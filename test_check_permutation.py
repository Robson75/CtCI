import check_permutation


def test_check_permutation():
    string1 = "test"
    string2 = "sett"
    assert check_permutation.check_permutation(string1, string2) is True
    string1 = "test"
    string2 = "sets"
    assert check_permutation.check_permutation(string1, string2) is False


def test_check_permutation_dict_chinese():
    string1 = "中文"
    string2 = "汉语"
    string3 = "文中"
    assert check_permutation.check_permutation_dict(string1, string2) is False
    assert check_permutation.check_permutation_dict(string1, string3) is True
