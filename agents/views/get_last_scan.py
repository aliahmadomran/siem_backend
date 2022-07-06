from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from ..controllers.get_last_scan import *


@api_view(['GET'])
def get_last_scan(request):
    try : 
        params = request.query_params
        responce = get_last_scan_controller(params)
        return JsonResponse(responce, status=status.HTTP_200_OK)

    except:
        return JsonResponse({"error message":"internal server error "}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)