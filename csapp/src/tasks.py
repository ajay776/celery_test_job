from __future__ import absolute_import, unicode_literals
from celery import shared_task
import time
from google_play_scraper import app
from .models import PlayStoreApp


@shared_task
def update_app_details():
    app_obj = PlayStoreApp.objects.filter(package_detail__isnull=True).first()
    if app_obj:
        result = app(app_obj.package_name)
        app_obj.package_detail = result
        app_obj.save()
        print(f"successfuly updated details of app: {app_obj.package_name}")
    else:print("all apps are updated")
    