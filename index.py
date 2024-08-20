def flatten(arr):
    if not isinstance(arr, list):
        return [arr]
    return [item for sublist in arr for item in flatten(sublist)]

def sort_array(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return sort_array(left) + middle + sort_array(right)

def flatten_and_sort(arr):
    return sort_array(flatten(arr))

nested_array = [3, [1, 2], [4, [5, 6]], 7]
result = flatten_and_sort(nested_array)
print(result)  # Output: [1, 2, 3, 4, 5, 6, 7]