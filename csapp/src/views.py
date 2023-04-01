from rest_framework.views import APIView
from rest_framework import generics
from .models import PlayStoreApp
from .serializer import PlayStoreSerializer
from rest_framework.response import Response
from rest_framework import renderers
import requests
from bs4 import BeautifulSoup


class PlayDataCreateView(APIView):
       
       def get(self, request):
              url =  "https://play.google.com/store/games?hl=en&gl=US"
              result = requests.get(url).text
              doc = BeautifulSoup(result, "html.parser")
              data = doc.prettify()
              heading = doc.find_all(class_ = "Si6A0c Gy4nib")
              for anchor in heading:
                     print(anchor['href'])
                     name = anchor['href'].split('=')[1]
                     app_obj = PlayStoreApp.objects.create(package_name=name)
              return Response("Data Stored Successfully")
       

class PlayStoreDataView(APIView):
              
       def get(self, request):
              data = PlayStoreApp.objects.all()
              serial = PlayStoreSerializer(data, many=True)
              return Response(serial.data)