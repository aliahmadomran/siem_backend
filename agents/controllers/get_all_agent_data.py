from ..services.get_all_agent_data import *

def get_all_agents_controller(params):
    response = get_all_agents_service(params['pretty'],params['sort'],params['limit'],params['status'],params['query'],params['select'])
    return response.json()