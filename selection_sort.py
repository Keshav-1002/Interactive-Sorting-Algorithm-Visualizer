import time

def selection_sort(data, draw_data, get_speed):
    n = len(data)
    
    for i in range(n):
        min_idx = i
        
        for j in range(i + 1, n):
            draw_data(data, optional_color='white', digit=j, digit2=min_idx, end=i-1)
            time.sleep(get_speed())
            
            if data[j] < data[min_idx]:
                min_idx = j
                
        data[i], data[min_idx] = data[min_idx], data[i]
        draw_data(data, optional_color='red', digit=i, digit2=min_idx, end=i)
        time.sleep(get_speed())

    draw_data(data, end=n-1)
    
