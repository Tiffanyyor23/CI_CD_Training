#!/usr/bin/env python3

import requests
import json

base_url = "https://webexapis.com/v1"
token = 'YTkwMzkxMDktYWQ0Zi00M2MxLWI0OWQtZWZhNTIzOTBkMDExYTUwODI3MGUtOGI2_P0A1_eb84e064-24b6-4877-a348-68ee377c32d0'

messages_url = "/messages"

headers = {
    "Accept":"application/json",
    "Content-Type":"application/json",
    "Authorization": "Bearer " + token
}

data = {
    "roomId": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vNjc1ODBmODAtMGExOC0xMWVjLTkxYzktMDUyMjBmN2JiOGFh",
    "text":"Your test run was successful"
}

response = requests.post(url=base_url+messages_url, headers=headers, data=json.dumps(data),verify=False)
print(response.status_code)
