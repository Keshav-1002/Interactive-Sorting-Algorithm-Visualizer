Sorting Algorithm Visualizer:
    This is an interactive Python application built with Tkinter that vividly demonstrates how various sorting algorithms work. It's a great        tool for anyone looking to understand sorting mechanics through dynamic visualization. Just input your own data, select an algorithm, and       watch the process unfold in real-time.

Technologies Used:
    Python 3
    Tkinter for GUI
    pyttsx3 for voice output
    winsound for sound cues
    Threading for smooth UI updates
    Time to analysis steps easily

Features:

Interactive Manual Input:
    Specify the number of elements you want to sort.
    Input each number manually with guided prompts.
    Easy error handling with speech + message box.

Multiple Algorithms to Explore:
Choose from a variety of popular sorting algorithms:
    Bubble Sort
    Selection Sort
    Quick Sort
    Merge Sort
    Count Sort (only supports non-negative integers)
    Radix Sort (only supports non-negative integers)
    Insertion Sort

Time Complexity at a Glance:
Displays the best, average, and worst-case time complexities for each algorithm right when you select it.

Real-Time Colorful Visualization:
    Data is represented as vertical bars.
    Colors change during comparisons, swaps, and on completion:
        Dynamic color cycling during sorting.
        Cyan color for sorted elements.
    Values are also displayed above bars for clarity.

Speech + Sound Feedback:
    Uses pyttsx3 for real-time voice guidance, error messages, and completion announcements.
    Sound alerts for valid input, errors, and successful sort.
    Keeps users engaged and informed.

Keyboard Accessibility:
Press Enter to trigger common actions:
    On No. of Elements input → starts input phase
    On element entry → adds current element
    On speed slider → handles input completion
This boosts accessibility and efficiency for keyboard users.

Use of Multithreading:
    Multithreading ensures the GUI never freezes.
    Sorting algorithms run in a separate thread so you can still interact with the interface while sorting happens in the background.
    pyttsx3 (text-to-speech) and messagebox are triggered via background threads, allowing both audio and popups to happen simultaneously           without delay.
    This keeps everything smooth and responsive, even during intensive operations.

Adjustable Speed Control:
    Use the slider to control animation speed.
    Slow it down to observe logic or speed up once familiar

Friendly Error Handling:
    Detects invalid inputs or incompatible values (e.g., negative numbers for Count Sort).
    Provides spoken feedback, message pop-ups, and sound alerts — all at once thanks to threading.

Reset Anytime:
    Want to start over with a new set of data or a different algorithm? Hit the Reset button and begin again effortlessly.

Bonus UX Touches:
    Validates if sorting algorithm is selected before adding elements.
    Warns if invalid data is entered (e.g., negative numbers in Count Sort).
    Updates label instructions dynamically to guide the user through every.

