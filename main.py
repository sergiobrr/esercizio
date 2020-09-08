"""
7Pixel techinical challenge
"""
__author__ = "Sergio Brero"
__version__ = "0.1.0"
__license__ = "MIT"


def get_min_number(array):
    """ Returns the min int which opposite is present into the list

    Params:
        array: list
    """
    positivi = []
    negativi = set()
    for x in array:
        if x < 0:
            negativi.add(x)
        else:
            positivi.append(x)

    positivi.sort(reverse=True)

    while positivi:
        num = positivi.pop()
        if -num in negativi:
            return num

    return 0
