import tweepy, time

CONSUMER_KEY = 'ZnFJoAvuD8e0hrBNk1BR2zNdZ'
CONSUMER_SECRET = 'iAqZBQhfxWhHyJiHzRrJKsv9zPu1qJZqlngDLZmBYEJKtRrHaA'
ACCESS_TOKEN = '974419809898323974-nY1hcpLYH7IAB9pjxhGmewgXyfDnlUC'
ACCESS_SECRET = 'jNcG3n22yNuAHyIF3511xYE1PMIbc6SOGloI10gChHdzb'


# configure our access information for reaching Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

i = 0

while True:
    api.update_status("Anime was a mistake " + str(i))
    print("Tweeting!")
    i = i + 1
    time.sleep(90) #Tweet every 2 minutes
    print("All done tweeting!")