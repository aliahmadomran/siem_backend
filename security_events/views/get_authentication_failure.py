from multiprocessing import Condition
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from ..controller.get_authentication_failure import *


@api_view(['GET'])
def get_authentication_failure(request):
    try : 
        params = request.query_params
        conditions = request.body
        responce = get_authentication_failure_controller(params,conditions)
        return JsonResponse(responce, status=status.HTTP_200_OK)

    except:
        return JsonResponse({"error message":"internal server error "}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)