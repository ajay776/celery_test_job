from rest_framework import serializers
from .models import PlayStoreApp

class PlayStoreSerializer(serializers.ModelSerializer):
#        Serailizer  for PlayStoreApp Model
       class Meta:
              model = PlayStoreApp
              fields = '__all__'
