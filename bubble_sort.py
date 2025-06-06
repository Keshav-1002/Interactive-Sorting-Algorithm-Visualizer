import time

def bubble_sort(data, draw_data, get_speed):
    n = len(data)
    
    for i in range(n - 1):
        swapped = False
        
        for j in range(n - 1 - i):
            draw_data(data, optional_color='white', digit=j, digit2=j+1)
            time.sleep(get_speed())
            
            if data[j] > data[j + 1]:   
                data[j], data[j + 1] = data[j + 1], data[j] 
                swapped = True
                continue
            
            draw_data(data, optional_color='red', digit=j, digit2=j+1)
            time.sleep(get_speed())
            
        if not swapped:  
            break
        
    draw_data(data, optional_color = 'cyan')
