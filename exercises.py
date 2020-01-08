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


if __name__ == '__main__':
    my_exercises = Exercises
    test_string = "I am a test string"
    palindrome_test = "I  mi"
    # print(urlify.urlify(test_string))
    print(palindrome_permutation(palindrome_test))
