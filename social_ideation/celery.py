from __future__ import absolute_import

import os

from celery import Celery

from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_ideation.settings')

ce_app = Celery('social_ideation')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
ce_app.config_from_object('django.conf:settings')
ce_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@ce_app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))