# -*- coding: utf-8 -*-
"""
Utility for generating placeholder images from http://lorempixum.com/
"""
COLOR_URL = 'http://lorempixum.com/%(width)s/%(height)s/'
GRAY_URL = 'http://lorempixum.com/g/%(width)s/%(height)s/'
CATEGORY_WHITELIST = [
    'abstract',
    'animals',
    'city',
    'food',
    'nightlife',
    'fashion',
    'people',
    'nature',
    'sports',
    'technics',
    'transport',
]


def get_url(width, height, color=True, category=None):
    """
    Craft the URL for a placeholder image.

    By default they are in color. To retrieve a grayscale image, set
    the color kwarg to False.

    To specify a photo from a specific category, pass it as 'category' kwarg.
    """
    d = dict(width=width, height=height)
    if color:
        url = COLOR_URL % d
    else:
        url = GRAY_URL % d
    if category:
        category = category.lower()
        if category not in CATEGORY_WHITELIST:
            raise ValueError("Submitted category is invalid")
        url = url + category
    return url
