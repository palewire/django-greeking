# -*- coding: utf-8 -*-
from django import template
register = template.Library()
from greeking.placekittens import get_url
from greeking.lorem_ipsum import words, paragraphs
from greeking.jabberwocky import get_grafs, get_html as get_jabberwocky_html
from greeking.pangrams import get_pangram, get_html as get_pangram_html
from greeking import quotables


class PlaceKittenNode(template.Node):
    def __init__(self, width=200, height=200, color=True):
        self.width = width
        self.height = height
        self.color = color
    
    def render(self, context):
        return '<img src="%s"/>' % get_url(self.width, self.height, color=self.color)


def placekitten(parser, token):
    """
    Creates an image of a random kitten at the provided width and height.
    
    Usage format:
        
        {% placekitten [width] [height] [gray] %}
        
    Example usage:
        
        Color image at 250 wide and 400 high
        {% placekitten 250 400 %}
        
        Grayscale image 100 wide and 100 high
        {% placekitten 100 100 gray %}
        
    """
    bits = list(token.split_contents())
    if len(bits) > 4 or len(bits) < 3:
        raise template.TemplateSyntaxError("Incorrect format")
    tagname, width, height = bits[:3]
    if len(bits) == 4:
        if bits[3] == 'gray':
            color = False
        else:
            raise template.TemplateSyntaxError("Incorrect format")
    else:
        color = True
    return PlaceKittenNode(width=width, height=height, color=color)
placekitten = register.tag(placekitten)


class CommentListNode(template.Node):
    def render(self, context):
        context['comment_list'] = quotables.get_comment_list()
        return ''


def greek_comment_list(parser, token):
    """ 
    Allows a template-level call of filler comments.

    Example usage:
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
    """
    return CommentListNode()
greek_comment_list = register.tag(greek_comment_list)


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
        return u'\n\n'.join(paras)


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
        raise template.TemplateSyntaxError("Incorrect format for %r tag" % tagname)
    return LoremNode(count, method, common)
lorem = register.tag(lorem)


class PangramNode(template.Node):
    def __init__(self, language):
        self.language = language

    def render(self, context):
        try:
            pangram = get_pangram(self.language)
        except KeyError:
            raise template.TemplateSyntaxError("Could not find a pangram for %r abbreviation" % self.language)
        return get_pangram_html(pangram)


#@register.tag
def pangram(parser, token):
    """
    Prints a pangram in the specified language.

    A pangram is a phrase that includes every letter of an alphabet.

    Default is English. For a full list of available languages, refer to pangrams.py

    Usage format::

        {% pangram [language] %}

    ``language`` is the two-letter abbreviation the desired language.

    Examples:
        * ``{% pangram %}`` will output the default English pangram.
        * ``{% pangram fr %}`` will output a French pangram.
    """
    bits = list(token.split_contents())
    tagname = bits[0]
    # Count bit
    if len(bits) > 1:
        language = bits[1]
    else:
        language = 'en'
    if len(bits) > 2:
        raise template.TemplateSyntaxError("Incorrect format for %r tag" % tagname)
    return PangramNode(language)
pangram = register.tag(pangram)


class JabberwockyNode(template.Node):
    def __init__(self, count):
        self.count = count

    def render(self, context):
        try:
            count = int(self.count)
        except (ValueError, TypeError):
            count = None
        return get_jabberwocky_html(get_grafs(count))


def jabberwocky(parser, token):
    """
    Prints paragraphs from Lewis Caroll's poem Jabberwocky for greeking in templates.

    Usage format::

        {% jabberwocky [count] %}

    ``count`` is a number (or variable) containing the number of paragraphs or
    words to generate (default is 7, which prints the entire poem).

    Examples:
        * ``{% jabberwocky %}`` will output the common "lorem ipsum" paragraph
        * ``{% jabberwocky 3 %}`` will output three paragraphs from the poem
    """
    bits = list(token.split_contents())
    tagname = bits[0]
    # Count bit
    if len(bits) > 1:
        count = bits[1]
    else:
        count = None
    if len(bits) > 2:
        raise template.TemplateSyntaxError("Incorrect format for %r tag" % tagname)
    return JabberwockyNode(count)
jabberwocky = register.tag(jabberwocky)
