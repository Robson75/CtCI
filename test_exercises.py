import exercises


def test_1_x_1_matrix():
    test_matrix = exercises.create_random_matrix(1, 1)
    assert exercises.rotate_matrix(test_matrix) == test_matrix


def test_2_x_2_matrix():
    test_matrix = [[1, 2],
                   [3, 4]]
    assert exercises.rotate_matrix(test_matrix) == [[3, 1],
                                                    [4, 2]]


def test_3_x_3_matrix():
    test_matrix = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]
    assert exercises.rotate_matrix(test_matrix) == [[7, 4, 1],
                                                    [8, 5, 2],
                                                    [9, 6, 3]]
