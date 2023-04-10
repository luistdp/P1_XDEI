from ngsiv2 import read_subcriptions
import json

def json_to_table(json_data):
    id = json_data["id"]
    description = json_data["description"]
    status = json_data["status"]
    entity_id_pattern = json_data["subject"]["entities"][0]["idPattern"]
    condition_attrs = json_data["subject"]["condition"]["attrs"]
    attributes = json_data["notification"]["attrs"]
    httpurl = json_data["notification"]["http"]["url"]
    metadata = json_data["notification"]["metadata"]
    if "throttling" in json_data:
        throttling = json_data["throttling"]
        print("id\tdescription\tstatus\tentity_id_pattern\tcondition_attrs\tattributes\thttpurl\tmetatdata\tthrottling")
        print(f"{id}\t{description}\t{status}\t{entity_id_pattern}\t{condition_attrs}\t{attributes}\t{httpurl}\t{metadata}\t{throttling}")
    else:
        print("id\tdescription\tstatus\tentity_id_pattern\tcondition_attrs\tattributes\thttpurl\tmetatdata\t")
        print(f"{id}\t{description}\t{status}\t{entity_id_pattern}\t{condition_attrs}\t{attributes}\t{httpurl}\t{metadata}\t")
    
status, data = read_subcriptions()

for json_data in data:
    json_to_table(json_data)
