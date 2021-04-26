import uuid
from datetime import date
import json

class ReviewHandler:
    def __init__(self, franchise, gameName, maxSize):
        self.reviews = []
        self.franchise = franchise
        self.gameName = gameName
        self.maxSize = maxSize

    def addReviews(self, reviews):
        reviewList = []
        for i in range(len(reviews)):
                thisReview = reviews[i]

                review = {}
                review['id'] = thisReview.get('recommendationid')
                review['author'] = str(uuid.uuid3(uuid.NAMESPACE_URL, thisReview.get('author').get('steamid')))
                review['date'] = str(date.fromtimestamp(thisReview.get('timestamp_created')))
                review['hours'] = thisReview.get('author').get('playtime_at_review')/60 #Using playtime at review because it's more useful than playtime_forever
                review['content'] = thisReview.get('review')
                review['comments'] = thisReview.get('comment_count')
                review['source'] = 'steam'
                review['helpful'] = thisReview.get('votes_up')
                review['funny'] = thisReview.get('votes_funny')
                review['recommended'] = thisReview.get('voted_up')
                review['franchise'] = self.franchise
                review['gameName'] = self.gameName
                reviewList.append(review)
        self.reviews.extend(reviewList)

    def saveReviews(self, filename):
        file = open(filename, 'w')
        file.write(json.dumps(self.reviews))
        file.close()
    
    def hasSpace(self, space):
        if self.maxSize > len(self.reviews) + space:
            return True
        else:
            return False

    def setReviewsEmpty(self):
        self.reviews = []
        