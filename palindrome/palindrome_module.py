def palindrome(string):
    original_str = string.lower().replace(' ', '')
    reversed_str = original_str[-1::-1]
    if original_str == reversed_str:
        return True
    else:
        return False


def main():
    in1 = input("")
    print(palindrome(in1))
    return


if __name__ == '__main__':
    main()
