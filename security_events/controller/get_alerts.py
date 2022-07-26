from get_alerts import  get_alerts_service


def get_alerts_conrtoller(params):
    responce = get_alerts_service(startDate=params["startDate"],endDate=params["endDate"],level=params["level"])
    return responce