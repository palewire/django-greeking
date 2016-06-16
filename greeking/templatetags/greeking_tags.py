# -*- coding: utf-8 -*-
import six
from django import template
from greeking import quotables
from django.utils.html import format_html
from greeking.lorem_ipsum import words, paragraphs
from greeking.fillmurray import get_url as get_fillmurray_url
from greeking.lorem_pixum import get_url as get_lorem_pixum_url
from greeking.placeholdit import get_url as get_placeholdit_url
from greeking.placekittens import get_url as get_placekitten_url
from greeking.pangrams import get_pangram, get_html as get_pangram_html
from greeking.jabberwocky import get_grafs, get_html as get_jabberwocky_html

register = template.Library()


@register.simple_tag
def fillmurray(width, height):
    """
    Creates a random image of Bill Murray at the provided width and height.

    Usage format:

        {% fillmurray [width] [height] %}

    Example usage:

        Color image at 250 wide and 400 high
        {% fillmurray 250 400 %}
    """
    url = get_fillmurray_url(width, height)
    return format_html('<img src="{}"/>', url)


@register.simple_tag
def lorem_pixum(width, height):
    """
    Creates a placeholder image at the provided width and height.

    Usage format:

        {% lorem_pixum [width] [height] %}

    Example usage:

        Color image at 250 wide and 400 high
        {% lorem_pixum 250 400 %}
    """
    url = get_lorem_pixum_url(width, height)
    return format_html('<img src="{}"/>', url)


@register.simple_tag
def placeholdit(
    width,
    height,
    background_color="cccccc",
    text_color="969696",
    text=None
):
    """
    Creates a placeholder image using placehold.it

    Usage format:

      {% placeholdit [width] [height] [background_color] [text_color] [text] %}

    Example usage:

        Default image at 250 square
        {% placeholdit 250 250 %}

        100 wide and 200 high
        {% placeholdit 100 200 %}

        Custom background and text colors
        {% placeholdit 100 200 background_color='fff' text_color=000' %}

        Custom text
        {% placeholdit 100 200 text='Hello LA' %}
    """
    url = get_placeholdit_url(
        width,
        height,
        background_color=background_color,
        text_color=text_color,
        text=text,
    )
    return format_html('<img src="{}"/>', url)


@register.simple_tag
def placekitten(width, height):
    """
    Creates an image of a random kitten at the provided width and height.

    Usage format:

        {% placekitten [width] [height] %}

    Example usage:

        Color image at 250 wide and 400 high
        {% placekitten 250 400 %}
    """
    url = get_placekitten_url(width, height)
    return format_html('<img src="{}"/>', url)


@register.simple_tag
def greek_comment_list():
    """
    Allows a template-level call of filler comments.

    Example usage:
    {% greek_comment_list as comment_list %}
    {% for comment in comment_list %}
        <div id="c{{ comment.id }}">
                <p>{{ comment.comment }}</p>
                <p>{{ comment.user_name }}</p>
                <p>{{ comment.submit_date|date:"F j, Y" }}</p>
                <p><a href="mailto:{{ comment.user_email }}">
                    {{ comment.user_email }}
                 </a></p>
                <p><a href="{{ comment.user_url }}">
                    {{ comment.user_url }}
                </a></p>
        </div>
    {% endfor %}
    """
    return quotables.get_comment_list()


class LoremNode(template.Node):
    def __init__(self, count, method, common):
        self.count, self.method, self.common = count, method, common

    def render(self, context):
        try:
            count = int(self.count.resolve(context))
        except (ValueError, TypeError):
            count = 1
        if self.method == 'w':
            return words(count, common=self.common)
        else:
            paras = paragraphs(count, common=self.common)
        if self.method == 'p':
            paras = ['<p>%s</p>' % p for p in paras]
        return six.text_type('\n\n'.join(paras))


def lorem(parser, token):
    """
    Creates random Latin text useful for providing test data in templates.

    Usage format::

        {% lorem [count] [method] [random] %}

    ``count`` is a number (or variable) containing the number of paragraphs or
    words to generate (default is 1).

    ``method`` is either ``w`` for words, ``p`` for HTML paragraphs, ``b`` for
    plain-text paragraph blocks (default is ``b``).

    ``random`` is the word ``random``, which if given, does not use the common
    paragraph (starting "Lorem ipsum dolor sit amet, consectetuer...").

    Examples:
        * ``{% lorem %}`` will output the common "lorem ipsum" paragraph
        * ``{% lorem 3 p %}`` will output the common "lorem ipsum" paragraph
          and two random paragraphs each wrapped in HTML ``<p>`` tags
        * ``{% lorem 2 w random %}`` will output two random latin words
    """
    bits = list(token.split_contents())
    tagname = bits[0]
    # Random bit
    common = bits[-1] != 'random'
    if not common:
        bits.pop()
    # Method bit
    if bits[-1] in ('w', 'p', 'b'):
        method = bits.pop()
    else:
        method = 'b'
    # Count bit
    if len(bits) > 1:
        count = bits.pop()
    else:
        count = '1'
    count = parser.compile_filter(count)
    if len(bits) != 1:
        raise template.TemplateSyntaxError(
            "Incorrect format for %r tag" % tagname
        )
    return LoremNode(count, method, common)
lorem = register.tag(lorem)


@register.simple_tag
def pangram(language='en'):
    """
    Prints a pangram in the specified language.

    A pangram is a phrase that includes every letter of an alphabet.

    Default is English. For a full list of available languages,
        refer to pangrams.py

    Usage format::

        {% pangram [language] %}

    ``language`` is the two-letter abbreviation the desired language.

    Examples:
        * ``{% pangram %}`` will output the default English pangram.
        * ``{% pangram 'fr' %}`` will output a French pangram.
    """
    try:
        pangram = get_pangram(language)
    except KeyError:
        raise template.TemplateSyntaxError(
            "Could not find a pangram for %r abbreviation" % language
        )
    return get_pangram_html(pangram)


@register.simple_tag
def jabberwocky(count=7):
    """
    Prints paragraphs from Lewis Caroll's poem Jabberwocky for greeking
    in templates.

    Usage format::

        {% jabberwocky [count] %}

    ``count`` is a number (or variable) containing the number of paragraphs or
    words to generate (default is 7, which prints the entire poem).

    Examples:
        * ``{% jabberwocky %}`` will output the common "lorem ipsum" paragraph
        * ``{% jabberwocky 3 %}`` will output three paragraphs from the poem
    """
    return get_jabberwocky_html(get_grafs(count or 7))
