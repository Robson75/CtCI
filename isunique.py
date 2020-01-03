def is_unique(s):
    char_list = []
    for c in s:
        if c in char_list:
            return False
        else:
            char_list.append(c)
    return True


def is_unique_2(s):
    table = [0] * (2**8)

    for c in s:
        code = ord(c)
        if table[code] == 1:
            return False
        else:
            table[code] = 1
    return True


class IsUnique:

    def __init__(self):
        pass


if __name__ == '__main__':
    isUnique = IsUnique()

    test_string = "sgd  j*"

    print(is_unique_2(test_string))
