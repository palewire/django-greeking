from setuptools import setup
from distutils.core import Command


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
                'default': {
                    'NAME': 'test.db',
                    'TEST_NAME': 'test.db',
                    'ENGINE': 'django.db.backends.sqlite3'
                }
            },
            INSTALLED_APPS=(
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.staticfiles',
                'greeking',
            ),
            TEMPLATES=[
                {
                    'BACKEND': 'django.template.backends.django.DjangoTemplates',
                    'DIRS': [],
                    'APP_DIRS': False,
                    'OPTIONS': {},
                },
            ]
        )
        from django.core.management import call_command
        import django
        django.setup()
        call_command('test', 'greeking')


setup(
    name='greeking',
    version='2.2.0',
    description='Django template tools for printing filler, a technique from the days of hot type known as greeking',
    author='Ben Welsh',
    author_email='b@palewi.re',
    url='http://django-greeking.readthedocs.io/',
    download_url='http://github.com/palewire/django-greeking.git',
    include_package_data=True,
    packages=(
        'greeking',
        'greeking.templatetags',
    ),
    license='MIT',
    keywords='greeking pangrams lorem ipsum quotables comments \
    text jabberwocky placekittens fillmurray filler',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Framework :: Django',
        'Framework :: Django :: 3',
        'Framework :: Django :: 4',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    cmdclass={'test': TestCommand}
)
