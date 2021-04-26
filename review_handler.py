import uuid
from datetime import date

class ReviewHandler:
    def __init__(self, reviews, franchise, gameName):
        self.reviews = reviews
        self.franchise = franchise
        self.gameName = gameName

    def somename(self):
        reviewList = []
        for i in range(len(self.reviews)):
            if i == 3:
                thisReview = self.reviews[i]
                print(self.reviews[i])
                print(self.reviews[i].get('recommendationid'))
                print(date.fromtimestamp(thisReview.get('timestamp_created')))

                review = {}
                review['id'] = thisReview.get('recommendationid')
                review['author'] = uuid.uuid3(uuid.NAMESPACE_URL, thisReview.get('author').get('steamid'))
                review['date'] = date.fromtimestamp(thisReview.get('timestamp_created'))
                review['hours'] = thisReview.get('playtime_at_review')/60 #Using playtime at review because it's more useful than playtime_forever
                review['content'] = thisReview.get('review')
                review['comments'] = thisReview.get('comment_count')
                review['source'] = 'steam'
                review['helpful'] = thisReview.get('votes_up')
                review['funny'] = thisReview.get('votes_funny')
                review['recommended'] = thisReview.get('voted_up')
                review['franchise'] = self.franchise
                review['gameName'] = self.gameName


    #def