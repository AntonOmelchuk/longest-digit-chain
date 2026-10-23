
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

