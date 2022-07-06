from django import template
from django.utils.html import format_html

from greeking import quotables
from greeking.fillmurray import get_url as get_fillmurray_url
from greeking.jabberwocky import get_grafs
from greeking.jabberwocky import get_html as get_jabberwocky_html
from greeking.latimes_ipsum import get_quote, get_story
from greeking.pangrams import get_html as get_pangram_html
from greeking.pangrams import get_pangram
from greeking.placekittens import get_url as get_placekitten_url

register = template.Library()


@register.simple_tag
def latimes_story():
    """
    Return an latimes_ipsum Story object, which has many possible variables,
    including slug, headline, byline, pub_date, canonical_url, kicker, description,
    sources, credits, and image (which are used for header images and has a default size of 900).

    Example:

        {% latimes_story as obj %}
            {{ obj.headline }}
            {{ obj.byline }}
            {{ obj.caption }}

    """
    return get_story()


@register.simple_tag
def latimes_quote():
    """
    Return an latimes_ipsum Quote object.

    Example:

        {% latimes_quote as obj %}
            {{ obj.quote }}
            {{ obj.source }}

    """
    return get_quote()


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


@register.simple_tag
def pangram(language="en"):
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
