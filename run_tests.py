"""
A bootstrap script that allows for easily testing this app outside of a full 
Django project.

Base on a script published by Lukasz Dziedzia at: 
http://stackoverflow.com/questions/3841725/how-to-launch-tests-for-django-reusable-app
"""

import os, sys
from django.conf import settings

DIRNAME = os.path.dirname(__file__)
settings.configure(
    DEBUG = True,
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(DIRNAME, 'database.db'),
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }
    },
    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
        'greeking',
    )
)


from django.test.simple import DjangoTestSuiteRunner

failures = DjangoTestSuiteRunner().run_tests(['greeking',], verbosity=1)
if failures:
    sys.exit(failures)
