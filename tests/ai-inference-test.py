#############################################################
# AEYE AI Test
# Created By Yoonchul Chung
# Created At 2024.08.03
# Welcome to Visit Github : https://github.com/Yoonchulchung
#############################################################

import requests
import json

url = 'http://localhost:6000/api/ai-inference' # AI Back

data = {"name" : "TEST"}
headers = {'Content-Type': 'application/json'}

json_data = json.dumps(data)

response = requests.post(url, data=data)

print(response.status_code)
print(response.json())