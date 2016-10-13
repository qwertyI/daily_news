import requests
import json

print requests.get('http://127.0.0.1:5001/cnblog').content
print type(requests.get('http://127.0.0.1:5001/cnblog').content)
content = requests.get('http://127.0.0.1:5001/cnblog').content
feed = json.loads(content)
print feed
print type(feed)
