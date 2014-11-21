<pre><code> _____   _____    _____   _____   _   _    _   __   _   _____
/  ___| |  _  \  | ____| | ____| | | / /  | | |  \ | | /  ___|
| |     | |_| |  | |__   | |__   | |/ /   | | |   \| | | |
| |  _  |  _  /  |  __|  |  __|  | |\ \   | | | |\   | | |  _
| |_| | | | \ \  | |___  | |___  | | \ \  | | | | \  | | |_| |
\_____/ |_|  \_\ |_____| |_____| |_|  \_\ |_| |_|  \_| \_____/</code></pre>

Django template tools for printing filler, a technique from the days of hot type known as greeking.

[![Build Status](https://travis-ci.org/palewire/django-greeking.png?branch=master)](https://travis-ci.org/palewire/django-greeking)
[![PyPI version](https://badge.fury.io/py/greeking.png)](http://badge.fury.io/py/greeking)
[![Coverage Status](https://coveralls.io/repos/palewire/django-greeking/badge.png?branch=master)](https://coveralls.io/r/palewire/django-greeking?branch=master)

* Documentation: [django-greeking.rtfd.org](http://django-greeking.rtfd.org/)
* Issues: [https://github.com/palewire/django-greeking/issues](https://github.com/palewire/django-greeking/issues)
* Packaging: [https://pypi.python.org/pypi/greeking](https://pypi.python.org/pypi/greeking)
* Testing: [https://travis-ci.org/palewire/django-greeking](https://travis-ci.org/palewire/django-greeking)
* Coverage: [https://coveralls.io/r/palewire/django-greeking](https://coveralls.io/r/palewire/django-greeking)

## Features

Currently, seven template tags are bundled into greeking. They can:

* Generate the lorem ipsum text already available in [django.contrib.webdesign](http://docs.djangoproject.com/en/dev/ref/contrib/webdesign/#ref-contrib-webdesign).
* Generate filler images from [lorempixum.com](http://lorempixum.com), [Fill Murray](http://www.fillmurray.com/), [placehold.it](http://placehold.it) and [placekitten.com](http://www.placekitten.com).
* Print snippets from Lewis Carroll's poem [Jabberwocky](http://en.wikipedia.org/wiki/Jabberwocky).
* Print pangrams in a variety of languages. A pangram is a phrase that includes every letter of an alphabet.
* Import an object_list of filler comments for use in greeking [Django's 'contrib' comments app](http://docs.djangoproject.com/en/dev/ref/contrib/comments/).clear
