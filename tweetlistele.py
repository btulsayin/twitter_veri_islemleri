# -*- coding: utf-8 -*-

import tweepy
#python tweepy kutuphanesi

consumer_key="your consumer_key... "
consumer_secret="your consumer secret_key... "
access_token="your access_token..."
access_token_secret="your access_token_secret..."

baglanti = tweepy.OAuthHandler(consumer_key, consumer_secret)
baglanti.set_access_token(access_token, access_token_secret)
api=tweepy.API(baglanti)
#baglanti saglanarak api degiskeni olusturulur.


tweets = api.home_timeline()
#anasayfadaki tweetler çekilir.

for tweet in tweets:
    print((tweet.text).encode("utf-8"))