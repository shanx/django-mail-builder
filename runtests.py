#!/usr/bin/env python

# Adapted from https://raw.githubusercontent.com/hzy/django-polarize/master/runtests.py

import sys

from django.conf import settings
from django.core.management import execute_from_command_line

import django


if not settings.configured:
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
            }
        },
        INSTALLED_APPS=(
            'django.contrib.contenttypes',
            'django.contrib.auth',
            'tests',
        ),
        MIDDLEWARE_CLASSES=[],
        ROOT_URLCONF='tests.urls',
        EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend',
        TEMPLATES=[
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [],
                'APP_DIRS': True,
            },
        ],
    )


def runtests():
    argv = sys.argv[:1] + ['test', 'tests']
    execute_from_command_line(argv)


if __name__ == '__main__':
    runtests()
