import time

def count_sort(arr, drawdata, speed):
    time_gap = speed()

    if not arr:
        return

    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    count = [0] * range_of_elements
    output = [0] * len(arr)

    for i in range(len(arr)):
        count[arr[i] - min_val] += 1
        drawdata(arr, optional_color='red', digit=i)
        time.sleep(time_gap)

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
        drawdata(arr, optional_color='white', digit=i)
        time.sleep(time_gap)

    for i in range(len(arr)):
        arr[i] = output[i]
        drawdata(arr, optional_color='green', digit=i)
        time.sleep(time_gap)
