def linear_search(arr, target):
    for i, each_num in enumerate(arr):
        if each_num == target:
            return i
    return -1

def main():
    arr = [1,2,3,4]
    target = 4
    res = linear_search(arr, target)
    if res == -1:
        print("Not found")
    else:
        print(f"{target} found at index {res}")


if __name__ == "__main__":
    main()