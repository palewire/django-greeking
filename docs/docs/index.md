# django-greeking

Django template tools for printing filler, a technique from the days of hot type known as greeking.

## Features

Currently, seven template tags are bundled into greeking. They can:

* Generate the lorem ipsum text already available in [django.contrib.webdesign](http://docs.djangoproject.com/en/dev/ref/contrib/webdesign/#ref-contrib-webdesign).
* Generate filler images from [lorempixum.com](http://lorempixum.com), [Fill Murray](http://www.fillmurray.com/), [placehold.it](http://placehold.it) and [placekitten.com](http://www.placekitten.com).
* Print snippets from Lewis Carroll's poem [Jabberwocky](http://en.wikipedia.org/wiki/Jabberwocky).
* Print pangrams in a variety of languages. A pangram is a phrase that includes every letter of an alphabet.
* Import an object_list of filler comments for use in greeking [Django's 'contrib' comments app](http://docs.djangoproject.com/en/dev/ref/contrib/comments/).

## Installation

```bash
pip install greeking
```

## Getting started

Before you can use any of the template tags, you have to add the app to the
``INSTALLED_APPS`` your settings.py file, like so:

```python
    'greeking',
```

And then import the library into your template.

```html+django
{% load greeking_tags %}
```

Then you just need to call out the tag you want to use.

Like Jabberywocky...

```html+django
{% jabberwocky 3 %}
```

...pangrams...

```html+django
{% pangram fr %}
```

...placeholder images...

```html+django
{% lorem_pixum 250 400 %}
```

```html+django
{% placeholdit 250 400 text='Hello' %}
```

...placekitten images...

```html+django
{% placekitten 200 200 %}
```

...Bill Murray images...

```html+django
{% fillmurray 200 200 %}
```

...or comments.

```html+django
{% greek_comment_list as comment_list %}
{% for comment in comment_list %}
    <div id="c{{ comment.id }}">
            <p>{{ comment.comment }}</p>
            <p>{{ comment.user_name }}</p>
            <p>{{ comment.submit_date|date:"F j, Y" }}</p>
            <p><a href="mailto:{{ comment.user_email }}">{{ comment.user_email }}</a></p>
            <p><a href="{{ comment.user_url }}">{{ comment.user_url }}</a></p>
    </div>
{% endfor %}
```

## Credits

* Pangrams are drawn from [Markus Kuhn](http://www.cl.cam.ac.uk/~mgk25/ucs/examples/quickbrown.txt).
* Comments drawn from the work of giants of our time.

## Other resources

* Issues: [https://github.com/palewire/django-greeking/issues](https://github.com/palewire/django-greeking/issues)
* Packaging: [https://pypi.python.org/pypi/greeking](https://pypi.python.org/pypi/greeking)
* Testing: [https://travis-ci.org/palewire/django-greeking](https://travis-ci.org/palewire/django-greeking)
* Coverage: [https://coveralls.io/r/palewire/django-greeking](https://coveralls.io/r/palewire/django-greeking)
