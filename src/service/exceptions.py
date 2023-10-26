class WaterTimeError(Exception):
    pass

class LangNotAvailableError(WaterTimeError):
    """
    When a language is not available
    """
    
class IntervalInvalidError(WaterTimeError):
    """
    When a interval time set is not a int and is an invalid value
    """
    
class IntervalNotSetError(WaterTimeError):
    """
    When interval time is not set
    """

class IntervalTypeError(WaterTimeError):
    """
    When interval type set is not valid
    """