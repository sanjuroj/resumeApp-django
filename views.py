import importlib
from django.shortcuts import render
from .models import *

from rest_framework import generics, serializers
from rest_framework.views import APIView
from rest_framework.response import Response



# Create your views here.



class APIAll (APIView): 

    def get(self, request):

        categories = ['Job', 'Basics', 'Education']
        modelsModule = importlib.import_module('.models','resume')

        
        responseArray = dict()

        for c in categories:

            modelObj = getattr(modelsModule, c)

            class TempSerializer(serializers.ModelSerializer):
                class Meta: 
                    model = modelObj


            serializer = TempSerializer(modelObj.objects.all(), many=True)
            #print(serializer.__repr__())
            responseArray[c.lower()] = serializer.data

        return Response(responseArray)

