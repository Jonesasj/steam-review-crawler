import urllib.request
import json
from review_handler import ReviewHandler
import sys

cursor = '*'
seenCursors = []
success = True
fileCounter = 0
MAX_REVIEW_FILE_LENGTH = 5000
NUM_PER_PAGE = 100
franchise = ""
gameName = ""
appId = ""

if len(sys.argv) != 4:
    sys.exit('the first argument should be franchise and the second should be game name')
else:
    franchise = sys.argv[1]
    gameName = sys.argv[2]
    appId = sys.argv[3]

cursor = '*'
seenCursors = []
success = True
fileCounter = 0
MAX_REVIEW_FILE_LENGTH = 5000
NUM_PER_PAGE = 100

handler = ReviewHandler(franchise, gameName, MAX_REVIEW_FILE_LENGTH)


while success == True:
    url = "https://store.steampowered.com/appreviews/" + str(appId) +"?json=1&num_per_page=" + str(NUM_PER_PAGE) + "&cursor=" + cursor

    req = urllib.request.Request(url=url, method='GET')
    with urllib.request.urlopen(req) as response:
        data = response.read()

    #print(data)
    jsonData = json.loads(data)
    cursor = jsonData.get('cursor')
    print(cursor)

    reviews = []
    #check if the query is successful
    if jsonData.get('success') == 1 and cursor not in seenCursors:
        seenCursors.append(cursor)
        reviews = jsonData.get('reviews')
        if handler.hasSpace(NUM_PER_PAGE):
            handler.addReviews(reviews)
        else:
            filename = 'output' + str(fileCounter) + '.json'
            handler.saveReviews(filename)
            handler.setReviewsEmpty()
            handler.addReviews(reviews)
            fileCounter = fileCounter + 1
    else:
        success = False

#Save remaining reviews
filename = 'output' + str(fileCounter) + '.json'
handler.saveReviews(filename)
