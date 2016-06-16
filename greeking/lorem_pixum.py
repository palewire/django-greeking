# -*- coding: utf-8 -*-
"""
Utility for generating placeholder images from http://lorempixum.com/
"""
URL = 'http://lorempixum.com/%(width)s/%(height)s/'


def get_url(width, height, color=True, category=None):
    """
    Craft the URL for a placeholder image.

    By default they are in color. To retrieve a grayscale image, set
    the color kwarg to False.

    To specify a photo from a specific category, pass it as 'category' kwarg.
    """
    d = dict(width=width, height=height)
    return URL % d
