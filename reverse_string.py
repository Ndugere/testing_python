def reverse_string(phrase = "This Is Africa"):
    list_of_char = list(phrase)

    right = len(list_of_char) - 1

    for left in range(len(list_of_char)):
        if left < right:
            list_of_char[left], list_of_char[right] = list_of_char[right], list_of_char[left]
            right -= 1
        else:
            break
   

    reversed_string = "".join(list_of_char)
    return reversed_string


def main():
    res = reverse_string()
    print(res)


if __name__ == "__main__":
    main()

        