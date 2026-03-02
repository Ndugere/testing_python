def duplicate_checker(arr: list) -> bool:
    seen = set()
    for each_item in arr:
        if each_item in seen:
            return True
        else:
            seen.add(each_item)
    return False


def main():
    print(duplicate_checker([1,2,3,4]))

main()