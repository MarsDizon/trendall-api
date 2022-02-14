# This file contains API views to access the ORM database
from django.shortcuts import render
from django.http.response import HttpResponse
from rest_framework import viewsets
from .serializers import VaseSerializer, PlateSerializer
from .models import Vase, Plate

# API view to retreive all attributes of a vase with given a vaseRef
class GetVase(viewsets.ModelViewSet):
    serializer_class = VaseSerializer
    def get_queryset(self):
        queryset = Vase.objects.all()
        vaseRef=self.request.query_params.get('vaseRef')
        try:
            if vaseRef is not None:
                queryset = queryset.filter(vaseRef=vaseRef)
            return queryset       
        except Exception as e:
            print(e)
            pass

# API view for Basic Search and Advanced Search, takes in a vase paramter (zero, 1 or many) passed through URL.
class FilterVases(viewsets.ModelViewSet):
    serializer_class = VaseSerializer 
    def get_queryset(self):
        queryset = Vase.objects.all()
        shapeName = self.request.query_params.get('shapeName') # Get shapeName parameter from URL 
        if shapeName is not None:
            try:
                queryset = queryset.filter(shapeName__icontains=shapeName)  # If shapeName in in database matches (full/partial) the searched dshapeName add it to queryset
            except Exception as e:
                print(e) # print any exceptions to log for debugging
        collectionName = self.request.query_params.get('collectionName')    # Get collectionName parameter from URL
        if collectionName is not None:
            try:
                queryset = queryset.filter(collectionName__icontains=collectionName) # If collectionName in in database matches (full/partial) the searched collectionName add it to queryset
            except Exception as e:
                print(e) #
        prevColl = self.request.query_params.get('previousCollection')      # Get previousCollection parameter from URL
        if prevColl is not None:
            try:
                queryset = queryset.filter(prevColl__icontains=prevColl)    # If previousCollection in in database matches (full/partial) the searched previousCollection, add it to queryset
            except Exception as e:
                print(e)
        artistName = self.request.query_params.get('artistName')            # Get artistName parameter from URL
        if artistName is not None:
            try:
                queryset = queryset.filter(artistName__icontains=artistName)        # If artistName in in database matches (full/partial) the searched artistName, add it to queryset
            except Exception as e:
                print(e)
                pass
        provenanceName = self.request.query_params.get('provenanceName')    # Get provenanceName parameter from URL
        if provenanceName is not None:
            try:
                queryset = queryset.filter(provenanceName__icontains=provenanceName) # If provenanceName in in database matches (full/partial) the searched proveanceName, add it to queryset
            except Exception as e:
                print(e)
                pass
        publications = self.request.query_params.get('publications')        # Get publications parameter from URL
        if publications is not None:
            try:
                queryset = queryset.filter(publications__icontains=publications)    # If publications in in database matches (full/partial) the searched publications, add it to queryset
            except Exception as e:
                print(e)
                pass    
        fabric = self.request.query_params.get('fabric')                    # Get fabric parameter from URL
        if fabric is not None:
            try:
                queryset = queryset.filter(fabric__icontains=fabric)        # If fabric in in database matches (full/partial) the searched fabric, add it to queryset
            except Exception as e:
                print(e)
                pass
        vaseRef = self.request.query_params.get('vaseRef')                  # Get vaseRef parameter from URL
        if vaseRef is not None:
            try:
                queryset = queryset.filter(vaseRef__icontains=vaseRef)      # If vaseRef in in database matches matches (full/partial) the searched vaseRef, add it to queryset
            except Exception as e:
                print(e)
                pass
        subject = self.request.query_params.get('subject')                  # Get subject parameter from URL
        if subject is not None:
            try:
                queryset = queryset.filter(subject__icontains=subject)      # If subjectin in database matches (full/partial) the searched subject, add it to queryset
            except Exception as e:
                print(e)
        return queryset 


# API view to retreive the plateRef using the vase_id passed as a URL parameter 
class GetPlate(viewsets.ModelViewSet):
    serializer_class = PlateSerializer 
    def get_queryset(self):
        queryset = Plate.objects.all()
        vase = self.request.query_params.get('vase')    # Get vaseRef parameter from URL
        if vase is not None:
            try:
                queryset = queryset.filter(vase=vase)   # If vaseRef matches vaseRef in database, return the data array
            except Exception as e:
                print(e)
        return queryset

def main(request):
    return HttpResponse("Hello")