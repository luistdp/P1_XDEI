import requests
import json
import pprint

base_path = 'http://localhost:1026/v2'

def list_entities(type = None, options = 'count', attrs = None):
    base_request = base_path + '/entities/'
    if options in ['count', 'keyValues','values']:
        base_request += f'?options={options}'
    if type is not None:
        base_request += f'&type={type}'
    if attrs is not None:
        base_request += f'&attrs={attrs}'
    r = requests.get(base_request)
    return (r.status_code, json.loads(r.text))

def read_entity(entity_id):
    r = requests.get(base_path + '/entities/' + entity_id)
    return (r.status_code, json.loads(r.text))

def items_for_entity(entity_id,entity_type):
    base_request = base_path + '/entities/' + \
    '?q='+ entity_type +'==' + entity_id + \
    '&options=count&type=InventoryItem'
    r = requests.get(base_request)
    return (r.status_code, json.loads(r.text))

def create_subscription(body):
    base_request = base_path + '/subscriptions/'
    headers = {
        "Content-Type":"application/json",
        "fiware-service":"openiot",
        "fiware-servicepath":"/"
    }
    r = requests.post(base_request, data=json.dumps(body), headers=headers)
    return r.status_code

def delete_subscription(subscription_id):
    base_request = base_path + f'/subscriptions/{subscription_id}'
    headers = {
        "fiware-service":"openiot",
        "fiware-servicepath":"/"
    }
    r = requests.delete(base_request,headers=headers)
    return r.status_code

def read_subcriptions():
    base_request = base_path + '/subscriptions/'
    headers = {
        "fiware-service":"openiot",
        "fiware-servicepath":"/"
    }
    r = requests.get(base_request, headers=headers)
    return (r.status_code, json.loads(r.text))
