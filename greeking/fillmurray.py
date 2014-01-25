# -*- coding: utf-8 -*-
"""
Utility for generating placeholder Bill Murray images
"""
COLOR_URL = 'http://www.fillmurray.com/%(width)s/%(height)s/'
GRAY_URL = 'http://www.fillmurray.com/g/%(width)s/%(height)s/'


def get_url(width, height, color=True):
    """
    Craft the URL for a placekitten image.

    By default they are in color. To retrieve a grayscale image, set
    the color kwarg to False.
    """
    d = dict(width=width, height=height)
    if color:
        return COLOR_URL % d
    else:
        return GRAY_URL % d
