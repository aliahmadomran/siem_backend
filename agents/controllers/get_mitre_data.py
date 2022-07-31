from ..services.get_mitre_data import *

def get_mitre_data_controller(params,conditions):
    response = get_mitre_data_service(startDate= params['startDate'],startDate= params['endDate'],conditions=conditions)
    return response.json()