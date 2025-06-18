import time

def insertion_sort(arr, drawdata, get_speed):
    drawdata(arr)
    time.sleep(get_speed())

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        drawdata(arr, digit=i, end=i-1)
        time.sleep(get_speed())

        while j >= 0 and arr[j] > key:
            drawdata(arr, digit=j, digit2=j+1, end=i-1)
            time.sleep(get_speed())

            arr[j + 1] = arr[j]
            j -= 1

            drawdata(arr, digit=j+1, end=i-1)
            time.sleep(get_speed())

        arr[j + 1] = key
        drawdata(arr, digit=j+1, end=i)
        time.sleep(get_speed())

    drawdata(arr, end=len(arr)-1)
    
