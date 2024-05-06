def linear_search(arr, target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

my_list = [4, 2, 6, 8, 1, 5]
target_element = 6
result = linear_search(my_list, target_element)
if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found.")
