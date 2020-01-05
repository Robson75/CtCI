class CheckPermutation:

    def __init__(self):
        pass


def check_permutation(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        table = [0] * (2 ** 16)
        for c in s1:
            code = ord(c)
            table[code] += 1
        for c in s2:
            code = ord(c)
            table[code] -= 1
        return all(i == 0 for i in table)
    return True


def check_permutation_dict(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        char_dict = {}
        for c in s1:
            if c not in char_dict:
                char_dict[c] = 1
            else:
                char_dict[c] += 1
        print(char_dict)
        for c in s2:
            if c not in char_dict:
                return False
            else:
                char_dict[c] -= 1
        print(char_dict)
        return all(value == 0 for value in char_dict.values())


if __name__ == '__main__':
    checkPermutation = CheckPermutation()
    test_string1 = "人美过"
    test_string2 = "美国人"
    test_string3 = "人美国"
    test_string4 = "more string"

    is_permutation = check_permutation_dict(test_string2, test_string3)

    print(is_permutation)
