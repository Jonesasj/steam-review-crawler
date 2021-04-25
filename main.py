import urllib.request
import json

franchise = "temp franchise name"
gameName = "temp game name"
url = "https://store.steampowered.com/appreviews/1382330?json=1"

req = urllib.request.Request(url=url, method='GET')
with urllib.request.urlopen(req) as response:
    data = response.read()

#print(data)
jsonData = json.loads(data)
print(jsonData)
print(type(jsonData))

reviews = []
#check if the query is successful
if jsonData.get('success') == 1:
    reviews = jsonData.get('reviews')

for i in range(len(reviews)):
    if i == 1:
        print(reviews[i])

#for i in range(len(jsonData)):
#    print(jsonData[i])