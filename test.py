from merge_sort import *
from thread import *


assert merge([2], [8]) == [2, 8]
assert merge([5], [3]) == [3, 5]
assert merge([2, 8], [3, 5]) == [2, 3, 5, 8]
assert merge([2, 3, 5, 8], [1, 4, 7, 9]) == [1, 2, 3, 4, 5, 7, 8, 9]


thread_manager = ThreadManager()
test_1 = ThreadWithReturnValue(
    target=merge_sort,
    name=thread_manager.get_new_thread_name(),
    args=(
        [2, 8, 5, 3, 9, 4, 1, 7],
        thread_manager,
    ),
)
test_1.start()
assert test_1.join() == [1, 2, 3, 4, 5, 7, 8, 9]


print("All tests passes")
