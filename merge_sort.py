import time

def merge(arr, l, m, r, drawdata, get_speed):
    n1 = m - l + 1
    n2 = r - m

    L = arr[l:m + 1]
    R = arr[m + 1:r + 1]

    i = j = 0
    k = l

    while i < n1 and j < n2:
        drawdata(arr, digit=l + i, digit2=m + 1 + j, end=l-1)
        time.sleep(get_speed())

        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
            
        else:
            arr[k] = R[j]
            j += 1

        drawdata(arr, digit=k, end=l-1)
        time.sleep(get_speed())
        k += 1

    while i < n1:
        arr[k] = L[i]
        drawdata(arr, digit=k, end=l-1)
        time.sleep(get_speed())
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        drawdata(arr, digit=k, end=l-1)
        time.sleep(get_speed())
        j += 1
        k += 1

    drawdata(arr, end=r)
    time.sleep(get_speed())

def merge_sort_recursive(arr, l, r, drawdata, get_speed):
    
    if l < r:
        m = (l + r) // 2

        merge_sort_recursive(arr, l, m, drawdata, get_speed)
        merge_sort_recursive(arr, m + 1, r, drawdata, get_speed)

        merge(arr, l, m, r, drawdata, get_speed)

def merge_sort(arr, drawdata, get_speed):
    drawdata(arr)
    time.sleep(get_speed())
    merge_sort_recursive(arr, 0, len(arr) - 1, drawdata, get_speed)

    drawdata(arr, end=len(arr)-1)
    
