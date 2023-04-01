from django.db import models


class PlayStoreApp(models.Model):
       package_name = models.CharField(max_length=1000)
       package_detail = models.JSONField(null=True)
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)