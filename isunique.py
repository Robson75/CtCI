def is_unique(s):
    char_list = []
    for c in s:
        if c in char_list:
            return False
        else:
            char_list.append(c)
    return True


class IsUnique:

    def __init__(self):
        pass


if __name__ == '__main__':
    isUnique = IsUnique()

    test_string = "sgj*"

    print(is_unique(test_string))
