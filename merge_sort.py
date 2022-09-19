from thread import *


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


def merge_sort(arr, thread_manager=None):
    if len(arr) == 1:
        return arr

    # Get the middle of array
    middle_index = len(arr) // 2

    # Divide arr to 2 halves
    left_arr = arr[:middle_index]
    right_arr = arr[middle_index:]

    # Sort each half
    left_arr = ThreadWithReturnValue(
        target=merge_sort,
        name=thread_manager.get_new_thread_name(),
        args=(
            left_arr,
            thread_manager,
        ),
    )
    right_arr = ThreadWithReturnValue(
        target=merge_sort,
        name=thread_manager.get_new_thread_name(),
        args=(
            right_arr,
            thread_manager,
        ),
    )

    left_arr.start()
    right_arr.start()

    left_arr = left_arr.join()
    right_arr = right_arr.join()

    # Merge
    return merge(left_arr, right_arr)
