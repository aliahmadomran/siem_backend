from ..services.get_agent_status import *

def get_agent_status_controller():
    response = get_agent_status_service()
    return response