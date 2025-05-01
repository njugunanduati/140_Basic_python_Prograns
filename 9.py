# rotate an list

def rotate_list(arr, d):
    n = len(arr)
    if d < 0 or d >= n:
        return "Invalid rotation value"
    
    rotated_arr = [0] * n
    for i in range(n):
        rotated_arr[i] = arr[(i + d) % n]
        print(rotated_arr)
    return rotated_arr

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    d = 3
    print(rotate_list(arr, d))