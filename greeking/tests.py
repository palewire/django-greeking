from django.template import Context, Template, TemplateSyntaxError
from django.test import TestCase


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
            "{% load greeking_tags %}{% jabberwocky foo bar %}",
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
            "{% load greeking_tags %}{% pangram foobar %}",
        )
        self.assertRaises(
            TemplateSyntaxError,
            self.render,
            "{% load greeking_tags %}{% pangram en foobar %}",
        )
        self.render("{% load greeking_tags %}{% pangram %}")

    def testGreekComments(self):
        """
        Tests the tag for pulling greek comments
        """
        from greeking import quotables

        t = "{% load greeking_tags %}{% greek_comment_list as comment_list %}"
        ctx, out = self.render(t)
        for comment in list(ctx["comment_list"]):
            comment_dict = {
                "user_name": comment.user_name,
                "user_email": comment.user_email,
                "user_url": comment.user_url,
                "comment": comment.comment,
                "submit_date": comment.submit_date,
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
        self.assertEqual(out, '<img src="http://www.fillmurray.com/200/200/"/>')
        self.assertRaises(
            TemplateSyntaxError,
            self.render,
            "{% load greeking_tags %}{% fillmurray foobar %}",
        )

    def testPlaceKittens(self):
        """
        Tests the tag for pulling placekitten images.
        """
        t1 = "{% load greeking_tags %}{% placekitten 200 200 %}"
        ctx, out = self.render(t1)
        self.assertEqual(out, '<img src="http://placekitten.com/200/200/"/>')
        self.assertRaises(
            TemplateSyntaxError,
            self.render,
            "{% load greeking_tags %}{% placekitten foobar %}",
        )

    def testLatimesIpsum(self):
        from greeking import latimes_ipsum

        story = latimes_ipsum.get_story()
        self.assertTrue(isinstance(story, latimes_ipsum.Story))
        self.assertTrue(isinstance(story.content, str))

        quote = latimes_ipsum.get_quote()
        self.assertTrue(isinstance(quote, latimes_ipsum.Quote))

        t4 = "{% load greeking_tags %}{% latimes_story as obj %}"
        ctx, out = self.render(t4)

        t5 = "{% load greeking_tags %}{% latimes_quote as obj %} \
        {{ obj.quote }} \
        {{ obj.source }}"
        ctx, out = self.render(t5)
