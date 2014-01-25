# -*- coding: utf-8 -*-
"""
Utility for generating placeholder kitten images
"""
COLOR_URL = 'http://placekitten.com/%(width)s/%(height)s/'
GRAY_URL = 'http://placekitten.com/g/%(width)s/%(height)s/'


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
