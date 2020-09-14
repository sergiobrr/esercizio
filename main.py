"""
7Pixel techinical challenge
"""
__author__ = "Sergio Brero"
__version__ = "0.1.0"
__license__ = "MIT"

MIN_VALUE = -100000
MAX_VALUE = 100000


class InvalidValue(ValueError):
    """Exception raised for errors in the array members.

    Attributes:
        value -- array member which caused the error
        index -- member's index
    """

    def __init__(
            self, value, index
    ):
        """
        Args:
            value: the invalid value
            index: invalid value list position
        """
        self.value = value
        self.index = index
        self.message = f'''Value "{value}" at position\
 {index} is not an integer between 100000 and -100000'''
        super().__init__(self.message)


def get_min_number(array):
    """ Returns the min int which opposite is present into the list
        or zero if conditions aren't matched

    Args:
        array: list

    Returns:
        num: int
    """
    positivi = []
    negativi = set()
    for x in array:
        if type(x) == int and 0 >= x >= MIN_VALUE:
            negativi.add(x)
        elif type(x) == int and 0 < x <= MAX_VALUE:
            positivi.append(x)
        else:
            raise InvalidValue(x, array.index(x))

    positivi.sort(reverse=True)

    while positivi:
        num = positivi.pop()
        if -num in negativi:
            return num

    return 0
