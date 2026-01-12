def binary_search_algo(target, arr):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1



def main():
    target = 7
    arr = [1,2,3,4,5]

    res = binary_search_algo(target, arr)

    if res == -1:
        print(f"{target} is not found in the arr")
    else:
        print(f"{target} found at index {res}")


if __name__ == "__main__":
    main()
