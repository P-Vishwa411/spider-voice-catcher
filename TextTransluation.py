import requests
import uuid
import json

# Add your key and endpoint
key = "replace your key"
endpoint = "replace your end point"

# location, also known as region.
# Required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
location = "replace your region"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',  
    'from': 'en',          
    'to': ['te', 'hi','gu','kn','ta']     
}

headers = {
    'Ocp-Apim-Subscription-Key': key,           
    'Ocp-Apim-Subscription-Region': location,  
    'Content-type': 'application/json',        
    'X-ClientTraceId': str(uuid.uuid4())      
}

# You can pass more than one object in the body.
body = [{
    'text': ' Hello, how are you? '
}]

# Making the POST request
request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

# Pretty-printing the response
print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
