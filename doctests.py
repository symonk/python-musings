
def example(x, y):
    """
    >>> example(10, 20)
    [20, 40]
    """
    return [i * 2 for i in (x, y)]


if __name__ == "__main__":
    from doctest import testmod
    testmod()