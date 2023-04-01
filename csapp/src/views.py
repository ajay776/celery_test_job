from rest_framework.views import APIView
from rest_framework import generics
from .models import PlayStoreApp
from .serializer import PlayStoreSerializer
from rest_framework.response import Response
from rest_framework import renderers
import requests
from bs4 import BeautifulSoup


class PlayDataCreateView(APIView):
       """"
       Api for inserting new app and if app allready in our DB then it will not insert it 
       """
       def get(self, request):
              url =  "https://play.google.com/store/games?hl=en&gl=US"
              result = requests.get(url).text
              doc = BeautifulSoup(result, "html.parser")
              data = doc.prettify()
              heading = doc.find_all(class_ = "Si6A0c Gy4nib")
              for anchor in heading:
                     print(anchor['href'])
                     name = anchor['href'].split('=')[1]
                     app = PlayStoreApp.objects.filter(package_name=name)
                     if not app.exists():
                            app_obj = PlayStoreApp.objects.create(package_name=name)
                     else: print("app already exists")
              return Response("Data Stored Successfully")
       

class PlayStoreDataView(APIView):
       '''
       Retrieve all the records present in our db for play store app
       '''
           
       def get(self, request):
              data = PlayStoreApp.objects.all()
              serial = PlayStoreSerializer(data, many=True)
              return Response(serial.data)
