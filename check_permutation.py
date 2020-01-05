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


if __name__ == '__main__':
    checkPermutation = CheckPermutation()
    test_string1 = "人美过"
    test_string2 = "美国人"
    test_string3 = "string test"
    test_string4 = "more string"

    is_permutation = check_permutation(test_string1, test_string2)

    print(is_permutation)
