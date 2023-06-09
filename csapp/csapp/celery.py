from __future__ import absolute_import, unicode_literals

from celery import Celery
from datetime import datetime, timedelta

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'csapp.settings')

app = Celery('celery_demo')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Scheduled a celery beat which excute every 15 seconds and fill our app details 
app.conf.beat_schedule = {
    'add-every-5-seconds': {
        'task': 'src.tasks.update_app_details',
        'schedule': 15,
    }
}

app.conf.timezone = 'UTC'

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
