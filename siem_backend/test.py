from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from siem_backend.dev import *
from network.siem_apis import *


@api_view(['GET'])
def return_token(request):
    
    token = getToken(host=dev_host,username=dev_username,password=dev_password)
    return JsonResponse({"token":token}, status=status.HTTP_200_OK)