from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from ..controllers.get_agent_status import *


@api_view(['GET'])
def get_agent_status(request):
    try : 
        responce = get_agent_status_controller()
        return JsonResponse(responce, status=status.HTTP_200_OK)

    except:
        return JsonResponse({"error message":"internal server error "}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)