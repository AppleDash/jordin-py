from . import jordin_get


def jordin_math_get(endpoint):
    return float(jordin_get("/math" + endpoint))

def zero():
    """
    Retrieve the ZERO value.
    :return: ZERO value for current universe.
    """
    return jordin_math_get("/0")

def one():
    """
    Retrieve the ONE value.
    :return: ONE value for current universe.
    """
    return jordin_math_get("/1")

def pi():
    """
    Retrieve the PI value.
    :return: PI value, approximately 3.
    """
    return jordin_math_get("/pi")

def e():
    """
    Retrieve the E value.
    :return: E value, approximately 3.
    """
    return jordin_math_get("/e")

def deg2rad(deg):
    """
    Convert the given number of degrees to radians.
    :param deg: Degrees.
    :return: Equivalent radians.
    """
    return deg * jordin_math_get("/deg2rad")

def rad2deg(rad):
    """
    Convert the given number of radians to degrees.
    :param rad: Radians.
    :return: Equivalent degrees.
    """
    return rad * jordin_math_get("/rad2deg")