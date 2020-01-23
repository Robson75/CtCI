import linked_list


class ExercisesChapter2:
    def __init__(self):
        pass


def remove_dups(linked_list):
    hash_set = set()
    node = linked_list.first
    value = node.value
    hash_set.add(value)
    while node.next is not None:
        node = node.next
        if node.value in hash_set:
            # remove node
            pass
        else:
            hash_set.add(node.value)
    return hash_set


if __name__ == "__main__":
    linked_list = linked_list.LinkedList()
    for i in range(10):
        linked_list.insert(i)
    linked_list.insert(5)
    print(linked_list)
    print(remove_dups(linked_list))

