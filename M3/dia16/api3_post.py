import requests
url = "https://jsonplaceholder.typicode.com/posts"
payload="{\n \"title\": \"Post 101\",\n \"body\": \"Este es nuestro primer post\"\n}"
headers = {
'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
print("")
print(response)#<Response [201]>