from email.quoprimime import body_check
import json
import requests
import urllib3
from base64 import b64encode
import json
def getToken(protocol='https',host='localhost',port=55000,username='',password='',login_endpoint= 'security/user/authenticate'):
    # Disable insecure https warnings (for self-signed SSL certificates)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # Configuration
    protocol = protocol
    host = host
    port = port
    username = username
    password = password
    login_endpoint = login_endpoint

    login_url = f"{protocol}://{host}:{port}/{login_endpoint}"
    basic_auth = f"{username}:{password}".encode()
    login_headers = {'Content-Type': 'application/json',
                    'Authorization': f'Basic {b64encode(basic_auth).decode()}'}

    # Login request 
    response = requests.get(login_url, headers=login_headers, verify=False)
    token = json.loads(response.content.decode())['data']['token']

    return token


def siemRequest(protocol='https',host='localhost',port=55000,username='',password='',request_type = 'get',api_endpoint ='',body={}):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    token = getToken(protocol=protocol,host=host,port=port,username=username,password=password)

    # New authorization header with the JWT token we got
    requests_headers = {'Content-Type': 'application/json',
                        'Authorization': f'Bearer {token}'}

    if request_type == 'get':
        response = requests.get(f"{protocol}://{host}:{port}/{api_endpoint}", headers=requests_headers, verify=False)
    
    return response


def getApiInfo(protocol='https',host='localhost',port=55000,username='',password=''):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    token = getToken(protocol=protocol,host=host,port=port,username=username,password=password)

    # New authorization header with the JWT token we got
    requests_headers = {'Content-Type': 'application/json',
                        'Authorization': f'Bearer {token}'}


    # Getting API information
    response = requests.get(f"{protocol}://{host}:{port}/?pretty=true", headers=requests_headers, verify=False)

    return response