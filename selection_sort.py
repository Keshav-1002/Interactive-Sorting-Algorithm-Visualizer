import time

def selection_sort(data, draw_data, get_speed):
    n = len(data)
    
    for i in range(n):
        min_idx = i
        draw_data(data, end=i-1, optional_color='white', digit=i)
        time.sleep(get_speed())
        
        for j in range(i + 1, n):
            draw_data(data, end=i-1, optional_color='white', digit=j, digit2=i)
            time.sleep(get_speed())
            
            if data[min_idx] > data[j]:
                min_idx = j
                draw_data(data, end=i-1, optional_color='red', digit=j, digit2=i)
                
        data[i], data[min_idx] = data[min_idx], data[i]
        
    draw_data(data, optional_color='cyan') 
