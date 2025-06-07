from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import threading
import winsound
from bubble_sort import bubble_sort
from quick_sort import quick_sort
from selection_sort import selection_sort
from merge_sort import merge_sort
from count_sort import count_sort

elements = []
current_index = 0
total_elements = 0

def start_input():
    global elements, current_index, total_elements
    
    try:
        total_elements = int(entry_n.get())
        
        if total_elements < 3:
            raise ValueError
        
        play_click_sound()
        elements.clear()
        current_index = 0
        update_prompt()
        
        entry_element.configure(state="normal")
        next_button.configure(state="normal")
        entry_n.configure(state="disabled")
        algo_select.configure(state="disabled")
        start_button.pack_forget()
        entry_element.focus_set()
        
    except ValueError:
        play_error_sound()
        messagebox.showerror("Input Error", 
                        "Please enter a valid number of elements (positive integer greater then 3).")

def reset_app():
    play_click_sound()
    global elements, current_index, total_elements
    elements.clear()
    current_index = 0
    total_elements = 0

    entry_n.configure(state="normal")
    algo_select.configure(state="readonly")
    entry_element.configure(state="disabled")
    next_button.configure(state="disabled")
    sort_button.configure(state="disabled")

    entry_n.delete(0, END)
    entry_element.delete(0, END)
    algo_select.current()
    speed.set(0.01)
    speed_slider.set(0.01)
    speed_slider.focus_set()
    prompt_label.config(text="Enter element:")

    for widget in canvas_frame.winfo_children():
        widget.destroy()

    canvas.delete("all")
    algo_display_label.config(text="")
    complexity_display_label.config(text="")

    start_button.pack_forget()
    start_button.pack(before=next_button, pady=(10, 5), fill="x")
    entry_n.focus_set()

def add_element():
    global current_index
    
    try:
        algo_display_label.configure(text=f"Selected Algorithm: {algo_select.get()}")
        val = int(entry_element.get())
        
        if algo_select.get() == "Count Sort" and val < 0:
            play_error_sound()
            messagebox.showerror("Invalid Input", "Count Sort only supports non-negative integers.")
            return

        play_click_sound()
        elements.append(val)
        draw_data(elements)
        current_index += 1
        entry_element.delete(0, END)
        
        if current_index < total_elements:
            update_prompt()
            
        else:
            entry_element.configure(state="disabled")
            next_button.configure(state="disabled")
            prompt_label.configure(text="All elements entered!")
            sort_button.configure(state="normal")
            speed_slider.configure(state="normal")
            messagebox.showinfo("Info", "All elements have been successfully entered!")
            speed_slider.focus_set()
            
    except ValueError:
        play_error_sound()
        messagebox.showerror("Input Error", "Please enter a valid integer.")

def update_prompt():
    prompt_label.config(text=f"Enter element {current_index + 1} of {total_elements}:")

def get_speed():
    return speed.get()

def play_click_sound():
    winsound.Beep(800, 75)

def play_success_sound():
    winsound.Beep(1000, 150)

def play_error_sound():
    winsound.Beep(400, 250)

algorithm_functions =   {
    "Bubble Sort": bubble_sort,
    "Quick Sort": quick_sort,
    "Selection Sort": selection_sort,
    "Merge Sort": merge_sort,
    "Count Sort": count_sort
                        }

def start_sorting():
    play_click_sound()
    selected_algo = algo_select.get()
    sort_func = algorithm_functions.get(selected_algo)
    sort_button.configure(state="disabled")
    speed_slider.configure(state="disabled")
    
    if sort_func is None:
        messagebox.showerror("Error", "No algorithm selected.")
        return

    def sort_thread():
        sort_func(elements, draw_data, get_speed)
        draw_data(elements, optional_color='cyan')
        play_success_sound()

    threading.Thread(target=sort_thread).start()
    
def on_enter_after_input():
    play_click_sound()
    
    if current_index >= total_elements and total_elements > 0:
        messagebox.showinfo("Info", "All elements have already been entered!")


root = Tk()
root.title("Interactive Sorting Algorithm Visualizer")
root.geometry("1400x800")
root.configure(bg="#f0f0f0")

title = Label(root, text="Sorting Algorithm Visualizer", font=("Arial", 22, "bold"), bg="#f0f0f0")
title.pack(pady=40)

main_frame = Frame(root, bg="#f0f0f0")
main_frame.pack(padx=20, pady=10, fill="both", expand=True)

visualization_frame = Frame(main_frame, bg="white", bd=2, relief="solid", width=500, height=200)
visualization_frame.pack(side="left", fill="both", expand=True, anchor="s")

algo_display_label = Label(visualization_frame, text="", font=("Arial", 14, "bold"), bg="white")
algo_display_label.pack(pady=5)

complexity_display_label = Label(visualization_frame, text="", font=("Arial", 13), bg="white")
complexity_display_label.pack(pady=(0, 5))

canvas_frame = Frame(visualization_frame, bg="white")
canvas_frame.pack(pady= (10, 0))

canvas = Canvas(visualization_frame, width=1100, height=500, bg="white")
canvas.pack(side="bottom", fill="both", expand=True)

def draw_data(data, optional_color='white', digit=None, digit2=None, end=None, var1=None, var2=None):
    canvas.delete("all")
    c_width = 1200
    c_height = 500
    x_width = c_width / (len(data) + 1)
    offset = 20
    spacing = 10
    max_data = max(data) if data else 1
    normalized_data = [i / max_data for i in data]

    for i, height in enumerate(normalized_data):
        x0 = i * x_width + offset
        y0 = c_height - height * 400
        x1 = (i + 1) * x_width
        y1 = c_height

        color = optional_color
        if digit is not None and i == digit:
            color = 'red'
            
        if digit2 is not None and i == digit2:
            color = 'blue'
            
        if end is not None and i > end:
            color = 'green'

        canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        canvas.create_text((x0 + x1) / 2, y0 - 10, text=str(data[i]), fill='black', font=("Arial", 10))

    for widget in canvas_frame.winfo_children():
        widget.destroy()
        
    for i, val in enumerate(data):
        label_color = optional_color
        
        if digit is not None and i == digit:
            label_color = 'red'
            
        if digit2 is not None and i == digit2:
            label_color = 'blue'
            
        if end is not None and i > end:
            label_color = 'green'

        label = Label(canvas_frame, text=str(val), bg=label_color, width=4, height=2, borderwidth=1,
                        relief="solid")
        label.grid(row=0, column=i, padx=5, pady=10)

    root.update_idletasks()

speed = DoubleVar(value=0.01)

controls_frame = Frame(main_frame, bg="#f0f0f0", width=200)
controls_frame.pack(side="right", fill="y", padx=20)
controls_frame.pack_propagate(False)

Label(controls_frame, text="Choose Algorithm:", bg="#f0f0f0", font=8).pack(anchor="w")
algo_select = ttk.Combobox(controls_frame, values=["Bubble Sort", "Selection Sort", "Quick Sort",
                            "Merge Sort", "Count Sort"], state="readonly")
algo_select.pack(fill="x", pady=(5,25))
algo_select.current()

def update_time_complexity(event):
    selected_algo = algo_select.get()
    time_complexities = {
        "Bubble Sort": "Time Complexity: O(n^2)",
        "Selection Sort": "Time Complexity: O(n^2)",
        "Quick Sort": "Time Complexity: O(n log n) average, O(n^2) worst",
        "Merge Sort": "Time Complexity: O(n log n)",
        "Count Sort": "Time Complexity: O(n + k)",
    }
    complexity_display_label.config(text=time_complexities.get(selected_algo, ""))

algo_select.bind("<<ComboboxSelected>>", update_time_complexity)
update_time_complexity(None)

Label(controls_frame, text="No. of Elements (n):", font=1, bg="#f0f0f0").pack(anchor="w")
entry_n = Entry(controls_frame)
entry_n.pack(fill="x", pady=(5,15))
entry_n.bind("<Return>", lambda event: start_input())

prompt_label = Label(controls_frame, text="Enter element:", bg="#f0f0f0", font=8)
prompt_label.pack(anchor="w", pady=(10, 0))

entry_element = Entry(controls_frame, state="disabled")
entry_element.pack(fill="x", pady=(5,10))
entry_element.bind("<Return>", lambda event: add_element())

start_button = Button(controls_frame, text="Start Input", command=start_input, font=8)
start_button.pack(pady=(10), fill="x")

next_button = Button(controls_frame, text="Next Element", command=add_element, state="disabled",font=8)
next_button.pack(pady=(5,15), fill="x")

Label(controls_frame, text="Speed (faster ← → slower):", bg="#f0f0f0").pack(anchor="w", pady=(10, 0))
speed_slider = Scale(controls_frame, from_=0.01, to=1, resolution=0.1, orient="horizontal",
                        variable=speed)
speed_slider.pack(fill="x", pady=5)
speed_slider.bind("<Return>", lambda event: on_enter_after_input())

sort_button = Button(controls_frame, text="Start Sorting", command=start_sorting, state="disabled",
                        font=8)
sort_button.pack(pady=10, fill="x")

reset_button = Button(controls_frame, text="Reset", command=reset_app, font=8)
reset_button.pack(pady=5, fill="x")

exit_button = Button(controls_frame, text="Exit", command=lambda: [play_click_sound(), root.destroy()],
                        font=8)
exit_button.pack(pady=5, fill="x")

entry_n.focus_set()

root.mainloop()
