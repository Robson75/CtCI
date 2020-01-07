class Urlify:
    def __init__(self):
        pass


def urlify(in_string):
    out_string = in_string.replace(" ", "%20")
    return out_string


def urlify2(in_string):
    out_string = ""
    for i in range(len(in_string)):
        if in_string[i] == " ":
            out_string += "%20"
        else:
            out_string += in_string[i]
    return out_string


if __name__ == '__main__':
    test_string = "Mr John Smith"
    result_string = urlify2(test_string)
    print(result_string)