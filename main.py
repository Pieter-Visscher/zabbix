import os
from dotenv import load_dotenv
import requests
import json
load_dotenv()

key=os.getenv("zabbix_key")
ZABBIX_API_URL=os.getenv("api_url")
source_hostname=os.getenv("hostname")

r = requests.post(ZABBIX_API_URL,
        json={
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "filter": {
                    "host": [
                        f"{source_hostname}",
                        ]
                    }
                },
            "id": 1,
            "auth": f"{key}"
            }
        )

data = json.loads(json.dumps(r.json()))

print(data['result'][0]['hostid'])
hostid = data['result'][0]['hostid']
host = data['result'][0]['host']

r = requests.post(ZABBIX_API_URL,
        json={
            "jsonrpc": "2.0",
            "method": "host.update",
            "params": {
                "hostid": f"{hostid}",
                "status": "1"
                },
            "id": 1,
            "auth": f"{key}"
            }
        )
print(f"host {host} with hostid {hostid} has been disabled")
print(json.loads(json.dumps(r.json())))
