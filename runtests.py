#!/usr/bin/env python
import sys
from django.conf import settings

def configure():

    from faker import Faker

    fake = Faker()

    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
                }
        },
        INSTALLED_APPS=(
            'django_faker',
            ),
        SITE_ID=1,
        SECRET_KEY=fake.sha1(),
        TEMPLATES = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'APP_DIRS': True,
                'OPTIONS': {},
            },
]
    )

if not settings.configured: configure()
import django
django.setup()


from django.test.utils import get_runner


def runtests():
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True, failfast=False)
    failures = test_runner.run_tests(['django_faker', ])
    sys.exit(failures)


if __name__ == '__main__':
    runtests()


