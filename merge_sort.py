import time

def merge(arr, l, m, r, drawdata, get_speed):
    n1 = m - l + 1
    n2 = r - m

    L = arr[l:m + 1]
    R = arr[m + 1:r + 1]

    i = j = 0
    k = l

    while i < n1 and j < n2:
        drawdata(arr, optional_color='yellow', digit=l + i, digit2=m + 1 + j)
        time.sleep(get_speed())

        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
            
        else:
            arr[k] = R[j]
            j += 1

        drawdata(arr, optional_color='red', digit=k)
        time.sleep(get_speed())

        k += 1

    while i < n1:
        arr[k] = L[i]

        drawdata(arr, optional_color='green', digit=k)
        time.sleep(get_speed())

        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]

        drawdata(arr, optional_color='green', digit=k)
        time.sleep(get_speed())

        j += 1
        k += 1

def merge_sort_recursive(arr, l, r, drawdata, get_speed):
    
    if l < r:
        m = (l + r) // 2

        merge_sort_recursive(arr, l, m, drawdata, get_speed)
        merge_sort_recursive(arr, m + 1, r, drawdata, get_speed)
        merge(arr, l, m, r, drawdata, get_speed)

def merge_sort(arr, drawdata, get_speed):
    merge_sort_recursive(arr, 0, len(arr) - 1, drawdata, get_speed)
    drawdata(arr, optional_color='cyan')
