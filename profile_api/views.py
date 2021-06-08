from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):

    def get(self, request, format=None):
        an_apiview = [
            'Uses standard HTTP methods',
            'Traditional Django View',
            'Gives you the most control over your logic',
            'mapped manually to urls'
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})
