from rest_framework import serializers, viewsets
from .models import *
import itertools
from rest_framework.response import Response
from rest_framework.decorators import api_view





# class JobSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Job
#         fields = ('company', 'position')




# class JobViewSet(viewsets.ModelViewSet):
#     ['Job', 'Education']
#     def list(self, request):
#         queryset = list(itertools.chain(Job.objects.all()))
#         serializer = JobSerializer(queryset, many=True)
#         return Response(serializer.data)
