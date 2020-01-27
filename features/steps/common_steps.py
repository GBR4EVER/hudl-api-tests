import base64
import json
import requests

from behave import when

dev = "https://hudl.com"
local = "http://localhost:8000"
host = local


@when('I post to the API')
def i_post_to_the_api(context):
    url = host + "/v1/schedule-api"
    if 'auth-token' not in context:
        context.auth_token = get_auth_token()
    headers = {
        'Content-Type': 'application/json',
        'cache-control': 'no-cache',
        'Authorization': 'Bearer ' + context.auth_token
    }
    context.result = requests.request("POST", url, data=context.json_request, headers=headers, verify=False)


def get_auth_token():
    url = "http://hudl.local.8080/oauth2/token"
    headers = {
        'Authorization': 'Basic ' + base64.b64decode(b'CORE@HUDL.OAUTH:23232323').decode('utf8'),
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    result = requests.post(url, headers=headers, data={'grant_type': 'client_credentials'}, verify=False)
    json_response = json.loads(result.text)
    return json_response['access-token']
