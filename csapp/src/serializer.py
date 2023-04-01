from rest_framework import serializers
from .models import PlayStoreApp

class PlayStoreSerializer(serializers.ModelSerializer):
       class Meta:
              model = PlayStoreApp
              fields = '__all__'