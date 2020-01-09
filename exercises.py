import urlify


class Exercises:
    def __init__(self):
        pass


def palindrome_permutation(in_string):
    s = in_string.replace(' ', '').lower()
    print(s)
    letters = {}
    for char in s:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1

    nr_of_odds = 0
    for key, value in letters.items():
        print(key, value)
        if value % 2 == 1:
            nr_of_odds += 1
    if nr_of_odds > 1:
        return False
    else:
        return True


def one_away(string1, string2):
    l1 = len(string1)
    l2 = len(string2)
    l_diff = l1 - l2
    if abs(l_diff) > 1:
        return False
    elif l_diff == 1:
        for i in range(l1):
            string1_sub = string1[:i] + string1[i+1:]
            if string1_sub == string2:
                return True
    elif l_diff == -1:
        for i in range(l2):
            string2_sub = string2[:i] + string2[i+1:]
            if string2_sub == string1:
                return True
    else:
        diffs = 0
        for i in range(l1):
            if string1[i] != string2[i]:
                diffs += 1
        if diffs <= 1:
            return True
    return False


if __name__ == '__main__':
    my_exercises = Exercises
    test_string = "I am a test string"
    palindrome_test = "I  mi"
    one_away_test_1 = "hello"
    one_away_test_2 = "heldu"
    # print(urlify.urlify(test_string))
    # print(palindrome_permutation(palindrome_test))
    print(one_away(one_away_test_1, one_away_test_2))
