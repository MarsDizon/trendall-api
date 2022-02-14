#this file contains URL endpoints for the backend for REST API's
from django.urls import path
from .views import main
from . import views


urlpatterns = [
    path('', main),
    path('getthevase/', views.GetTheVase.as_view(), name="getthevase"), #API endpoint to get all the attributes for a vase
    path('searchresults/', views.FilterVases.as_view(), name="searchresults"), #API endpoint to retreive all vases matching parameters passed in the URL
    path('getplate/', views.GetPlate.as_view(), name="getplate") #API endpoint to get all plateRef's (if any) from plate table using vaseRef
]
