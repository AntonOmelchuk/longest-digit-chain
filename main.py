from collections import defaultdict


def load_data(filename: str) -> list[str]:
    """
    Load data from file
    :param filename - path to file
    :return: list[str] - list with data
    """
    with open(filename, 'r') as f:
        content = f.read()

    raw_data = content.split()

    return raw_data


def build_graph(fragments: list[str]):
    """
    Creates dict where:
    key: first two digits of fragment
    value: list of fragments idx that start with these digits
    Ex: If chain needs '92' - can easy find it by using by_prefix['92']
    """
    by_prefix = defaultdict(list)
    for idx, fragment in enumerate(fragments):
        by_prefix[fragment[:2]].append(idx)


    """
    Creates adjacency list for all fragments
    For each fragment take last 2 digits (suffix) and use 
    prefix idx to find all valid next options excluding self-references
    Ex: 1st fragment (0 idx) has sufix '17', fragment with prefix '17'
        has idx - 37, so in adjacency_list for first fragment we save
        this idx 37 as potential next fragment  
    """
    adjacency_list = []
    for idx, fragment in enumerate(fragments):
        suffix = fragment[-2:]
        valid_options = by_prefix[suffix]
        not_self_reference = [i for i in valid_options if i != idx]
        adjacency_list.append(not_self_reference)

    """
    Sort adjacency list
    For each fragment sort its next candidate in 
    desc order based on number of their own outgoing branches 
    Ex: If adjacency_list[5] has options [12, 3, 45] with 2, 0, and 5 outgoing 
      branches respectively, sort them to [45, 12, 3] so 
      the algorithm explores the most promising branch first
    """
    for i in range(len(fragments)):
        adjacency_list[i].sort(key=lambda j: len(adjacency_list[j]), reverse=True)

    return adjacency_list


build_graph(load_data("data.txt"))
