class ExercisesChapter2:
    def __init__(self):
        pass


def remove_dups(linked_list):
    hash_set = set()
    for nr in linked_list:
        if nr in hash_set:
            # remove node
            pass
        else:
            hash_set.add(nr)
    return hash_set


if __name__ == "__main__":
    not_a_linked_list = [i for i in range(10)]
    not_a_linked_list[5] = 1
    print(not_a_linked_list)
    print(remove_dups(not_a_linked_list))

