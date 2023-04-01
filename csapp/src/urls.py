from django.urls import path
from .views import *

urlpatterns = [
    path('', PlayStoreDataView.as_view()),
    path('create_data', PlayDataCreateView.as_view())
]
