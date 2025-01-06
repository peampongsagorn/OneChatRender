import requests
import json

token = "A41118f4c3901504599cd424f489f0bc6f378f8f35e9b45c1b5b5a77d77e14635c345d3bb654c428fa7ac1aa7ddf7f8cc"
url = "https://chat-api.one.th/manage/api/v1/getlistroom"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {token}"
}

parameter = {
	"bot_id":"B334b547016f659f5b75ec45af18f3e38"
}
response = requests.post(url, headers=headers, data= json.dumps(parameter))
print(f"Status: {response.status_code}, Response: {response.text}") 