from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from ..controllers.get_all_agent_data import *


@api_view(['GET'])
def get_all_agent(request):
    try : 
        params = request.query_params
        responce = get_all_agents_controller(params)
        return JsonResponse(responce, safe=False, status=status.HTTP_200_OK)

    except:
        return JsonResponse({"error message":"internal server error "}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)