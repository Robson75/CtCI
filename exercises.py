import urlify
import random
import numpy


class Exercises:
    def __init__(self):
        pass


def palindrome_permutation(in_string):
    """Check if a string could be permuted into a palindrome."""
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
    """Check if two strings differ buy maximum 1 character."""
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


def string_compression(in_string):
    char_old = in_string[0]
    count = 1
    compression_list = [str(count) + char_old]
    list_index = 0
    for char in in_string[1:]:
        if char == char_old:
            count += 1
            compression_list[list_index] = str(count) + char_old
        else:
            char_old = char
            count = 1
            compression_list.append(str(count) + char_old)
            list_index += 1
    compressed_string = ""
    for i in range(len(compression_list)):
        compressed_string += compression_list[i]
    if len(compressed_string) < len(in_string):
        return compressed_string
    else:
        return in_string


def create_random_matrix(columns, rows):
    """Create and return a m x n matrix filled with random values."""
    return [[random.randrange(10) for c in range(columns)] for r in range(rows)]


def rotate_matrix(in_matrix):
    """Rotate a n x n matrix clockwise 90 degrees."""
    rows = len(in_matrix)
    columns = len(in_matrix[0])
    for row in range(len(in_matrix)):
        print(in_matrix[row])

    print()
    for c in range(int(columns/2)):
        for r in range(c, rows - c - 1):
            # 90 degree forward rotation
            # 4 values shift place each round
            temp_value = in_matrix[c][r]
            new_c, new_r = compute_shift(c, r, columns)
            in_matrix[c][r] = in_matrix[new_c][new_r]
            new2_c, new2_r = compute_shift(new_c, new_r, columns)
            in_matrix[new_c][new_r] = in_matrix[new2_c][new2_r]
            new3_c, new3_r = compute_shift(new2_c, new2_r, columns)
            in_matrix[new2_c][new2_r] = in_matrix[new3_c][new3_r]
            in_matrix[new3_c][new3_r] = temp_value

    for row in range(len(in_matrix)):
        print(in_matrix[row])
    return in_matrix


def compute_shift(x, y, n):
    new_x = n - y - 1
    new_y = x
    # print(new_x, new_y)
    return new_x, new_y


def zero_matrix(matrix):
    """Put all values in any row and column that has a zero in it to zero."""
    rows = len(matrix)
    columns = len(matrix[0])
    # create two sets to keep all rows and columns that will be put to zero
    zero_rows = set()
    zero_columns = set()
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == 0:
                zero_columns.add(i)
                zero_rows.add(j)
    for i in zero_columns:
        for j in range(rows):
            matrix[i][j] = 0
    for j in zero_rows:
        for i in range(columns):
            matrix[i][j] = 0
    return matrix


def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    for i, char in enumerate(s2):
        if char == s1[0]:
            s2_rotated = s2[i:] + s2[:i]
            # print(s2_rotated)
            if s2_rotated == s1:
                return True
    return False


def is_rotation2(s1, s2):
    if len(s1) != len(s2):
        return False
    if s2 in (s1 + s1):
        return True
    return False


if __name__ == '__main__':
    my_exercises = Exercises
    test_string = "I am a test string"
    palindrome_test = "I dd mi"
    one_away_test_1 = "hello"
    one_away_test_2 = "heldu"
    string_compression_test = "helloteeeeeeeeeeeest"
    rotate_matrix_test = create_random_matrix(4, 4)
    # print(urlify.urlify(test_string))
    print(palindrome_permutation(palindrome_test))
    # print(one_away(one_away_test_1, one_away_test_2))
    # print(string_compression(string_compression_test))
    # rotate_matrix(rotate_matrix_test)
    in_matrix = create_random_matrix(4, 4)
    # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in in_matrix]))
    # print()
    zero_put_matrix = zero_matrix(in_matrix)
    # print(zero_put_matrix)
    # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in zero_put_matrix]))
    rotate_string_test1 = "waterball"
    rotate_string_test2 = "erballwat"
    print(is_rotation2(rotate_string_test1, rotate_string_test2))

    import timeit
    print(timeit.timeit("is_rotation", setup="from __main__ import is_rotation", number=1000))

