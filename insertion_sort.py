import time

def insertion_sort(data, draw_data, get_speed):
    n = len(data)
    
    for i in range(1, n):
        key = data[i]
        j = i - 1

        draw_data(data, end=i-1, optional_color='white', digit=i)
        time.sleep(get_speed())

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            
            draw_data(data, end=i-1, optional_color='red', digit=j, digit2=j+1)
            time.sleep(get_speed())
            
            j -= 1

        data[j + 1] = key

        draw_data(data, end=i, optional_color='white', digit=j+1)
        time.sleep(get_speed())

    draw_data(data, optional_color='cyan')
