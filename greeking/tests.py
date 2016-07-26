import six
from django.test import TestCase
from django.template import Template, Context, TemplateSyntaxError


class GreekingTemplateTagTests(TestCase):

    def render(self, t, **c):
        ctx = Context(c)
        out = Template(t).render(ctx)
        return ctx, out

    def testJabberwocky(self):
        """
        Tests the tag for pulling jabberwocky
        """
        from greeking.jabberwocky import get_grafs, get_html
        graph_range = list(range(1, 8))
        for graphs in graph_range:
            t = "{% load greeking_tags %}{% jabberwocky " + str(graphs) + " %}"
            ctx, out = self.render(t)
            match = get_html(get_grafs(graphs))
            self.assertEqual(out, match)
        self.render("{% load greeking_tags %}{% jabberwocky foobar %}")
        self.render("{% load greeking_tags %}{% jabberwocky %}")
        self.assertRaises(
            TemplateSyntaxError,
            self.render,
            "{% load greeking_tags %}{% jabberwocky foo bar %}"
        )

    def testPangrams(self):
        """
        Tests the tag for pulling pangrams
        """
        from greeking.pangrams import PANGRAMS
        languages = list(PANGRAMS.keys())
        for language in languages:
            t = "{% load greeking_tags %}{% pangram '" + language + "' %}"
            self.render(t)
        self.assertRaises(
            TemplateSyntaxError,
            self.render,
            "{% load greeking_tags %}{% pangram foobar %}"
        )
        self.assertRaises(
            TemplateSyntaxError,
            self.render,
            "{% load greeking_tags %}{% pangram en foobar %}"
        )
        self.render("{% load greeking_tags %}{% pangram %}")

    def testGreekComments(self):
        """
        Tests the tag for pulling greek comments
        """
        from greeking import quotables
        t = "{% load greeking_tags %}{% greek_comment_list as comment_list %}"
        ctx, out = self.render(t)
        for comment in list(ctx['comment_list']):
            comment_dict = {
                'user_name': comment.user_name,
                'user_email': comment.user_email,
                'user_url': comment.user_url,
                'comment': comment.comment,
                'submit_date': comment.submit_date
            }
            match = quotables.HIPHOP[comment.comment_id]
            for k, v in list(comment_dict.items()):
                self.assertEqual(v, match[k])

    def testFillMuray(self):
        """
        Tests the tag for pulling Bill Murray images.
        """
        t1 = "{% load greeking_tags %}{% fillmurray 200 200 %}"
        ctx, out = self.render(t1)
        self.assertEqual(
            out,
            '<img src="http://www.fillmurray.com/200/200/"/>'
        )
        self.assertRaises(
            TemplateSyntaxError,
            self.render,
            "{% load greeking_tags %}{% fillmurray foobar %}"
        )

    def testPlaceholdIt(self):
        """
        Tests the tag for pulling placehold.it images.
        """
        t1 = "{% load greeking_tags %}{% placeholdit 250 250 %}"
        ctx, out = self.render(t1)
        self.assertEqual(
            out, u'<img src="http://placehold.it/250x250/cccccc/969696/"/>'
        )
        t2 = "{% load greeking_tags %}{% placeholdit 100 200 %}"
        ctx, out = self.render(t2)
        self.assertEqual(
            out, u'<img src="http://placehold.it/100x200/cccccc/969696/"/>'
        )
        t3 = "{% load greeking_tags %}{% placeholdit 100 200 \
background_color='fff' text_color='000' %}"
        ctx, out = self.render(t3)
        self.assertEqual(
            out, u'<img src="http://placehold.it/100x200/fff/000/"/>'
        )
        t4 = "{% load greeking_tags %}{% placeholdit 100 200 \
text='Hello LA' %}"
        ctx, out = self.render(t4)
        self.assertEqual(
            out, u'<img src="http://placehold.it/100x200/cccccc/969696/\
?text=Hello+LA"/>'
        )
        t5 = "{% load greeking_tags %}{% placeholdit 100 200 'fff' \
'000' 'Hello LA' %}"
        ctx, out = self.render(t5)
        self.assertEqual(
            out,
            u'<img src="http://placehold.it/100x200/fff/000/?text=Hello+LA"/>'
        )
        self.assertRaises(
            TemplateSyntaxError,
            self.render,
            "{% load greeking_tags %}{% placeholdit foobar %}"
        )
        self.assertRaises(
            TemplateSyntaxError,
            self.render,
            "{% load greeking_tags %}{% placeholdit 200 200 b a b c d e%}"
        )

    def testPlaceKittens(self):
        """
        Tests the tag for pulling placekitten images.
        """
        t1 = "{% load greeking_tags %}{% placekitten 200 200 %}"
        ctx, out = self.render(t1)
        self.assertEqual(out, u'<img src="http://placekitten.com/200/200/"/>')
        self.assertRaises(
            TemplateSyntaxError,
            self.render,
            "{% load greeking_tags %}{% placekitten foobar %}"
        )

    def testLoremIpsum(self):
        """
        Tests the tag for pulling lorem ipsum
        """
        t1 = "{% load greeking_tags %}{% lorem %}"
        ctx, out = self.render(t1)
        self.assertEqual(
            out,
            'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do\
 eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim\
 veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea\
 commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit\
 esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat\
 cupidatat non proident, sunt in culpa qui officia deserunt mollit anim\
 id est laborum.'
        )
        t2 = "{% load greeking_tags %}{% lorem 3 p %}"
        self.render(t2)
        t3 = "{% load greeking_tags %}{% lorem 3 w %}"
        self.render(t3)
        t4 = "{% load greeking_tags %}{% lorem 3 b %}"
        self.render(t4)
        t5 = "{% load greeking_tags %}{% lorem 3 p random %}"
        self.render(t5)
        t6 = "{% load greeking_tags %}{% lorem 3 w random %}"
        self.render(t6)
        t7 = "{% load greeking_tags %}{% lorem a p %}"
        self.render(t7)
        self.assertRaises(
            TemplateSyntaxError,
            self.render,
            "{% load greeking_tags %}{% lorem 1 p random foobar %}"
        )

    def testLoremPixum(self):
        """
        Tests the tag for pulling lorem pixum images.
        """
        t1 = "{% load greeking_tags %}{% lorem_pixum 200 200 %}"
        ctx, out = self.render(t1)
        self.assertEqual(
            out,
            '<img src="http://lorempixum.com/200/200/"/>'
        )
        self.assertRaises(
            TemplateSyntaxError,
            self.render,
            "{% load greeking_tags %}{% lorem_pixum foobar %}"
        )

    def testLatimesIpsum(self):
        from greeking import latimes_ipsum

        story = latimes_ipsum.get_story()
        self.assertTrue(isinstance(story, latimes_ipsum.Story))
        self.assertTrue(isinstance(story.content, six.string_types))

        related_items = latimes_ipsum.get_related_items()
        self.assertTrue(isinstance(related_items[0], latimes_ipsum.RelatedItem))
        self.assertTrue(len(related_items) == 4)
        self.assertTrue(len(latimes_ipsum.get_related_items(1)) == 1)
