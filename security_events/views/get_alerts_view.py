from security_events.controller.get_alerts import get_alerts_conrtoller
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view




@api_view(['GET'])
def get_alerts(request):
    try : 

        params = request.query_params
        responce = get_alerts_conrtoller(params)
        # return JsonResponse({"count":response.json()["count"]}, safe=False, status=status.HTTP_200_OK)
        return JsonResponse(responce, safe=False, status=status.HTTP_200_OK)

    except:
        return JsonResponse({"error message":"internal server error "}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)