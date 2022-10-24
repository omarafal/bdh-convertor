class NotCorrectInputTypeError(Exception):
    """Raised when the type of number entered is not the expected type"""
    pass


class NotAValidNumberFormatError(Exception):
    """
    Raised when the number entered is not valid
    Example: 25..5
    """
    pass