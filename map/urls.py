# urls.py

from django.urls import path
from .views import AccidentMapView, AccidentMapJsonView
app_name = 'map'
urlpatterns = [
    path("map/", AccidentMapView.as_view(), name='accident_map'),
    path('api/map/data/', AccidentMapJsonView.as_view(), name='accident_map_json'),
]