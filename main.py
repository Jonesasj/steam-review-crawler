import urllib.request
import json
from review_handler import ReviewHandler

REVIEW_SIZE_LIMIT = 5000
franchise = "temp franchise name"
gameName = "temp game name"
url = "https://store.steampowered.com/appreviews/1382330?json=1"

req = urllib.request.Request(url=url, method='GET')
with urllib.request.urlopen(req) as response:
    data = response.read()

#print(data)
jsonData = json.loads(data)

reviews = []
#check if the query is successful
if jsonData.get('success') == 1:
    reviews = jsonData.get('reviews')

handler = ReviewHandler(reviews)
handler.somename()

#for i in range(len(jsonData)):
#    print(jsonData[i])