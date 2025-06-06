import time

def partition(arr, low, high, draw_data, get_speed):
    i = (low - 1)
    pivot = arr[high] 

    for j in range(low, high):
        draw_data(arr, digit=j, digit2=high, optional_color='white', var1=low, var2=high)
        time.sleep(get_speed())
        
        if arr[j] <= pivot: 
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            draw_data(arr, digit=j, digit2=i, optional_color='red', var1=low, var2=high)
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    draw_data(arr, digit=i+1, digit2=high, optional_color='red', var1=low, var2=high)
    
    time.sleep(get_speed())
    return i + 1

def quickSortA(arr, low, high, draw_data, get_speed):
    
    if low < high:
        pi = partition(arr, low, high, draw_data, get_speed)

        quickSortA(arr, low, pi - 1, draw_data, get_speed)
        quickSortA(arr, pi + 1, high, draw_data, get_speed)

def quick_sort(data, draw_data, get_speed):
    quickSortA(data, 0, len(data) - 1, draw_data, get_speed)
    draw_data(data, optional_color='cyan')
