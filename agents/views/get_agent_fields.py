from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from ..controllers.get_agent_status import *


@api_view(['GET'])
def get_agent_fields(request):

    
    try : 
        responce = [
                    "dateAdd",
                    "lastKeepAlive",
                    "name",
                    "manager",
                    "ip",
                    "version",
                    "id",
                    "status",
                    "node_name",
                    "registerIP",
                    "os.arch",
                    "os.major",
                    "os.minor",
                    "os.name",
                    "os.platform",
                    "os.uname",
                    "os.version",
                    "os.build"
                ]
        
        return JsonResponse(responce, safe=False, status=status.HTTP_200_OK)

    except:
        return JsonResponse({"error message":"internal server error "}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)