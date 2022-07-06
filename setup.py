import os
from distutils.core import Command

from setuptools import setup


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


def version_scheme(version):
    """
    Version scheme hack for setuptools_scm.

    Appears to be necessary to due to the bug documented here: https://github.com/pypa/setuptools_scm/issues/342

    If that issue is resolved, this method can be removed.
    """
    import time

    from setuptools_scm.version import guess_next_version

    if version.exact:
        return version.format_with("{tag}")
    else:
        _super_value = version.format_next_version(guess_next_version)
        now = int(time.time())
        return _super_value + str(now)


def local_version(version):
    """
    Local version scheme hack for setuptools_scm.

    Appears to be necessary to due to the bug documented here: https://github.com/pypa/setuptools_scm/issues/342

    If that issue is resolved, this method can be removed.
    """
    return ""


class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from django.conf import settings

        settings.configure(
            DATABASES={
                "default": {
                    "NAME": "test.db",
                    "TEST_NAME": "test.db",
                    "ENGINE": "django.db.backends.sqlite3",
                }
            },
            INSTALLED_APPS=(
                "django.contrib.auth",
                "django.contrib.contenttypes",
                "django.contrib.sessions",
                "django.contrib.staticfiles",
                "greeking",
            ),
            TEMPLATES=[
                {
                    "BACKEND": "django.template.backends.django.DjangoTemplates",
                    "DIRS": [],
                    "APP_DIRS": False,
                    "OPTIONS": {},
                },
            ],
        )
        import django
        from django.core.management import call_command

        django.setup()
        call_command("test", "greeking")


setup(
    name="greeking",
    description="Django template tools for printing filler, a technique from the days of hot type known as greeking",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Ben Welsh",
    author_email="b@palewi.re",
    url="https://palewi.re/docs/django-greeking/",
    include_package_data=True,
    packages=(
        "greeking",
        "greeking.templatetags",
    ),
    license="MIT",
    keywords="greeking pangrams lorem ipsum quotables comments text jabberwocky placekittens fillmurray filler",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Framework :: Django",
        "Framework :: Django :: 3",
        "Framework :: Django :: 4",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    cmdclass={"test": TestCommand},
    setup_requires=["setuptools_scm"],
    use_scm_version={"version_scheme": version_scheme, "local_scheme": local_version},
    project_urls={
        "Documentation": "https://palewi.re/docs/django-greeking/",
        "Source": "https://github.com/datadesk/django-greeking/",
        "Tracker": "https://github.com/datadesk/django-greeking/issues",
    },
)
