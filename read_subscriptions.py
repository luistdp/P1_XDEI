from ngsiv2 import read_subcriptions
import json
status, data = read_subcriptions()
print(json.dumps(data,indent = 4))