import requests
import json 

base_path = 'http://localhost:1026/v2'

payload = {
    "lock": {
    "type":"command",
    "value": ""
    }
        
    }
headers = {
    "Content-Type":"application/json",
    "fiware-service":"openiot",
    "fiware-servicepath":"/"
}
for i in range(4):
    base_request = base_path + f'/entities/Door:00{i+1}/attrs'
    r = requests.patch(base_request, data=json.dumps(payload), headers=headers)
    if r.status_code == 204:
        print(f"Door:00{i+1} cerrada")

print("\n")
payload = {
  "off": {
      "type" : "command",
      "value" : ""
  }
}

for i in range(4):
    base_request = base_path + f'/entities/Lamp:00{i+1}/attrs'
    r = requests.patch(base_request, data=json.dumps(payload), headers=headers)
    if r.status_code == 204:
        print(f"Lamp:00{i+1} apagada")