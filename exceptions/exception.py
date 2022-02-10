class Error(Exception):
    pass


class AttributeError(Error):
    pass


class ValueIllegal(Error):
    """Raised when the value is incompatible for example the value is albums but needed artists"""
    pass
