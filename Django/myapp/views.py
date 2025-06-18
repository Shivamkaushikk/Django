from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

# Optional: In-memory storage
DATA_STORE = []

def check_api_key(request):
    api_key = request.headers.get('X-API-KEY')
    return api_key == settings.API_KEY

@api_view(['GET', 'POST'])
def my_api(request):
    if not check_api_key(request):
        return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        return Response(DATA_STORE)

    elif request.method == 'POST':
        content = request.data.get('message')
        if content:
            DATA_STORE.append({'message': content})
            return Response({'status': 'Message received!'}, status=status.HTTP_201_CREATED)
        return Response({'error': 'No message provided'}, status=status.HTTP_400_BAD_REQUEST)
