# django-greeking

Django template tools for printing filler, a technique from the days of hot type known as greeking.


## Features

Greeking can:

* Generate filler images from [placehold.it](http://placehold.it), [placekitten.com](http://www.placekitten.com) and [Fill Murray](http://www.fillmurray.com/).
* Print pangrams in a variety of languages. A pangram is a phrase that includes every letter of an alphabet.
* Create ``Story``, ``Image``, ``RelatedItem`` and ``Quote`` objects with boilerplate text, URLs and a set of the attributes common to news.
* Print snippets from Lewis Carroll's poem [Jabberwocky](http://en.wikipedia.org/wiki/Jabberwocky).
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


## Placeholder images

All placeholder providers expect a width and height to be provided.

One provider we have a templatetag for is [placehold.it](https://placehold.it/).

```html+django
{% placeholdit 400 250 %}
```

<img src="https://placeholdit.imgix.net/~text?txtsize=38&txt=400%C3%97250&w=400&h=250">

Another is [placekitten.com](https://placekitten.com/)

```html+django
{% placekitten 200 200 %}
```

<img src="https://placekitten.com/200/200">


Another is fillmurray.com

```html+django
{% fillmurray 600 200 %}
```

<img src="http://www.fillmurray.com/600/200">

### Customizing images

The placeholdit tag allows for the text over the image to be customized, as well as the text and background colors.

```html+django
{% placeholdit 400 250 text='Hello' %}
```

<img src="https://placeholdit.imgix.net/~text?txtsize=38&txt=Hello&w=400&h=250&txttrack=0">

```html+django
{% placeholdit 400 250 background_color='fff' text_color='000' %}
```

<img src="https://placeholdit.imgix.net/~text?txtsize=38&bg=ffffff&txtclr=000000&txt=400%C3%97250&w=400&h=250">

## Pangrams

A pangram is a phrase that includes every letter of an alphabet. It is useful when testing font implementations.

By default, an English pangram is returned.

```html+django
{% pangram %}
```

> The quick brown fox jumps over the lazy dog.

A set of other language are available, including Japanese, Spanish, French and German. They can be called by providing
the language code like so:

```html+django
{% pangram 'de' %}
```

> Falsches Üben von Xylophonmusik quält jeden größeren Zwerg.


## Los Angeles Times ipsum

A set of objects with boilerplate text, URLs and a set of the attributes common to news.

The library can generate ``Story``, ``Image``, ``RelatedItem`` and ``Quote`` objects.

They should be assigned to variables in the template and then printed out as needed.

### Story objects

```html+django
{% latimes_story as obj %}

<h1>{{ obj.headline }}</h1>
<div>
    {{ obj.byline }}
</div>
```

Which would print out as:

```html
<h1>This is not a headline</h1>
<div>This is not a byline</div>
```

### Image objects


### Quote objects


### Related item lists



To use latimes_ipsum, include the latimes_ipsum objects like so:

```html+django
def latimes_ipsum(request):
    """
    A context processor to include lorem ipsum objects from the
    Los Angeles Times.
    """
    from greeking import latimes_ipsum
    latimes_ipsum.get_story()
    latimes_ipsum.get_related_items(4)
    latimes_ipsum.get_image(250)

```


## Jabberwocky

<img height=300 style="float:right; margin-left: 15px;" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Jabberwocky.jpg/800px-Jabberwocky.jpg">

["Jabberywocky"](https://en.wikipedia.org/wiki/Jabberwocky) is a 1871 poem by Lewis Carroll, the author of "Alice in Wonderland." Selections can be printed by using the tag below.
The number of paragraphs can be optionally provided to limit its length. The poem has seven paragraphs in total.

```html+django
{% jabberwocky 3 %}
```

> 'Twas brillig, and the slithy toves
Did gyre and gimble in the wabe;
All mimsy were the borogoves,
And the mome raths outgrabe.

> "Beware the Jabberwock, my son!
The jaws that bite, the claws that catch!
Beware the Jubjub bird, and shun
The frumious Bandersnatch!"

> He took his vorpal sword in hand:
Long time the manxome foe he sought-
So rested he by the Tumtum tree,
And stood awhile in thought.


## Comments

An object_list of filler comments for use in greeking content for Django's [popular comments application](https://github.com/django/django-contrib-comments).

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

* Repo: [https://github.com/palewire/django-greeking](https://github.com/palewire/django-greeking)
* Issues: [https://github.com/palewire/django-greeking/issues](https://github.com/palewire/django-greeking/issues)
* Packaging: [https://pypi.python.org/pypi/greeking](https://pypi.python.org/pypi/greeking)
* Testing: [https://travis-ci.org/palewire/django-greeking](https://travis-ci.org/palewire/django-greeking)
* Coverage: [https://coveralls.io/r/palewire/django-greeking](https://coveralls.io/r/palewire/django-greeking)
