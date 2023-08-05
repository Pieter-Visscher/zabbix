import os
from dotenv import load_dotenv
import requests
import json
load_dotenv()
key=os.getenv("zabbix_key")

ZABBIX_API_URL = "https://zabbix.pvisscher.nl/api_jsonrpc.php"

#response = requests.get(
#        'https://zabbix.pvisscher.nl/api_jsonrpc.php', headers={'Authorization': f'access_token {key}','Content-Type': 'application/json'}
#        )
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

print(json.dumps(r.json(), indent = 4, sort_keys=True))

