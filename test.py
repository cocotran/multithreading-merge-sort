from merge_sort import *

assert(merge([2],  [8]) == [2, 8])
assert(merge([5],  [3]) == [3, 5])
assert(merge([2, 8],  [3, 5]) == [2, 3, 5, 8])
assert(merge([2, 3, 5, 8],  [1, 4, 7, 9]) == [1, 2, 3, 4, 5, 7, 8, 9])
assert(merge_sort([2, 8, 5, 3, 9, 4, 1, 7]) == [1, 2, 3, 4, 5, 7, 8, 9])

print("All tests passes")