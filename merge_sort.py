def merge(arr_a, arr_b):
    temp_arr = []

    # Compare 2 arrays and add to temp array
    while arr_a and arr_b:
        if arr_a[0] > arr_b[0]:
            temp_arr.append(arr_b.pop(0))
        else:
            temp_arr.append(arr_a.pop(0))

    # At this point either arr_a or arr_b is emppty
    # join them and return temp_arr
    temp_arr = temp_arr + arr_a + arr_b
    return temp_arr
        

def merge_sort(arr):
    if len(arr) == 1:
        return arr

    # Get the middle of array
    middle_index = len(arr) // 2

    # Divide arr to 2 halves
    left_arr = arr[:middle_index]
    right_arr = arr[middle_index:]

    # Sort each half
    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)

    # Merge
    return merge(left_arr, right_arr)


