# find the largest element in a list

def find_largest(arr):
    if len(arr) == 0:
        return 0
    return max(arr)

def find_smallest(arr):
    if len(arr) == 0:
        return 0
    return min(arr)

def find_largest_element(arr):
    if len(arr) == 0:
        return 0
    
    largest = arr[0]
    for i in arr:
        if i > largest:
            largest = i
    return largest

def find_smallest_element(arr):
    if len(arr) == 0:
        return 0
    
    smallest = arr[0]
    for i in arr:
        if i < smallest:
            smallest = i
    return smallest

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(find_largest(arr))
    print(find_smallest(arr))
    print(find_largest_element(arr))
    print(find_smallest_element(arr))