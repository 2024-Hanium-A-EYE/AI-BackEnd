import requests
import json

# Test if AI is working well
# Test -> AI Back -> AI OpticNET -> AI Back -> Test
# Good Test == "GOOD"
# Bad Test == "BAD"

# Everything is json

url = 'http://localhost:6000/api/ai-inference' # AI Back

data = {"name" : "TEST"}
headers = {'Content-Type': 'application/json'}

json_data = json.dumps(data)

response = requests.post(url, data=data)

print(response.status_code)
print(response.json())