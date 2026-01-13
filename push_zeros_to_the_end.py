def push_zeros_to_the_end(arr):

    left = 0

    for right in range(len(arr)):
        if arr[right] != 0:
            arr[right], arr[left] = arr[left], arr[right]
            left += 1
    
    return arr


def main():
    arr = [8,9, 0, 10,2,0,4,5,6]
    res = push_zeros_to_the_end(arr)
    print(res)

if __name__ == "__main__":
    main()