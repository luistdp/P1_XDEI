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

def list_inventory_items_for_product(product_id):
    base_request = base_path + '/entities/' + \
    '?q=refProduct==' + product_id + '&attrs=id' + \
    '&options=keyValues&type=InventoryItem'
    r = requests.get(base_request)
    return (r.status_code, json.loads(r.text))