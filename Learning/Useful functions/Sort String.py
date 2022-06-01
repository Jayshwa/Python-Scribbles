def sort_string(param):
    """
    Sorts string into alphabetical order.
    """
    return " ".join(sorted(param.split(), key=str.casefold))

