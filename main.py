import os
from dotenv import load_dotenv
import requests
import json
load_dotenv()
key=os.getenv("zabbix_key")
ZABBIX_API_URL=os.getenv("api_url")

r = requests.post(ZABBIX_API_URL,
        json={
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "filter": {
                    "host": [
                        "artoria",
                        "debian"
                        ]
                    }
                },
            "id": 1,
            "auth": f"{key}"
            })

#print(json.dumps(r.json(), indent = 4, sort_keys=True))
#print(json.dumps(r.json([0]['result']["hostid"])))

result = json.dumps(r.json())

print(result[0]["result"]["hostid"])

