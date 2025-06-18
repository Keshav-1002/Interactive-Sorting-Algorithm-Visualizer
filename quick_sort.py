import time

def quick_sort(data, draw_data, get_speed):
    
    def _quick_sort(data, low, high):
        
        if low < high:
            pi = partition(data, low, high)
            _quick_sort(data, low, pi - 1)
            _quick_sort(data, pi + 1, high)
    
    def partition(data, low, high):
        pivot = data[high]
        i = low - 1
        
        for j in range(low, high):
            draw_data(data, optional_color='white', digit=j, digit2=high, end=high)
            time.sleep(get_speed())
            
            if data[j] <= pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
                draw_data(data, optional_color='red', digit=i, digit2=j, end=high)
                time.sleep(get_speed())
        
        data[i + 1], data[high] = data[high], data[i + 1]
        draw_data(data, optional_color='red', digit=i+1, digit2=high, end=high)
        time.sleep(get_speed())
        return i + 1
    
    _quick_sort(data, 0, len(data) - 1)
    draw_data(data, end=len(data)-1)
    
