import requests

url = "https://jsonplaceholder.typicode.com/users/1"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response)#<Response [200]>