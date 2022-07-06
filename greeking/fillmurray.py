"""
Utility for generating placeholder Bill Murray images
"""
URL = "http://www.fillmurray.com/%(width)s/%(height)s/"


def get_url(width, height, color=True):
    """
    Craft the URL for a placekitten image.

    By default they are in color. To retrieve a grayscale image, set
    the color kwarg to False.
    """
    d = dict(width=width, height=height)
    return URL % d
