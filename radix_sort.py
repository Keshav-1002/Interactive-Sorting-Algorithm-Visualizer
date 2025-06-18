import time

def counting_sort_for_radix(arr, exp, drawdata, get_speed):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
        drawdata(arr, digit=i, digit2=i, end=-1)
        time.sleep(get_speed())

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n-1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        drawdata(arr, digit=i, digit2=count[index], end=-1)
        time.sleep(get_speed())

    for i in range(n):
        arr[i] = output[i]
        drawdata(arr, digit=i, end=i)
        time.sleep(get_speed())

def radix_sort(arr, drawdata, get_speed):
    drawdata(arr)
    time.sleep(get_speed())

    max_num = max(arr)
    exp = 1
    
    while max_num // exp > 0:
        drawdata(arr, end=-1)
        time.sleep(get_speed())
        
        counting_sort_for_radix(arr, exp, drawdata, get_speed)

        drawdata(arr, end=len(arr)-1)
        time.sleep(get_speed())
        
        exp *= 10

    drawdata(arr, end=len(arr)-1)
    
