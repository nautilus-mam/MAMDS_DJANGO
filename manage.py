#!/usr/bin/env python
"""
    Django's command-line utility for administrative tasks.
        Create a Django Project --> django-admin startproject <project-name>> .
            The dot indicate the new project should be created in actual directory and do not create a new root
                directory.
    To rn django project in a terminal -> python manage.py runserver
"""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MAMDS_Django.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
