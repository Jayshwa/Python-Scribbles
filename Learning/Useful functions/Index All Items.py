example = [[0, 1, 2], [1, 2, 3], [4, 5]]


def index_all(search_list, item):
    """
    Searches the list for all items defined as "item".
    Maps out where in the list that item is located.
    """
    indices = list()
    for i in range(len(search_list)):
        if search_list[i] == item:
            indices.append([i])
        elif isinstance(search_list[i], list):
            for index in index_all(search_list[i], item):
                indices.append([i] + index)
    return indices


print(index_all(example, 2))
