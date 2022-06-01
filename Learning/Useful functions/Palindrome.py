def is_palindrome(param):
    """
    Checks if palindrome, returns bool
    """
    if not isinstance(param, str):
        return "Must be a string"
    else:
        return param == param[::-1]

