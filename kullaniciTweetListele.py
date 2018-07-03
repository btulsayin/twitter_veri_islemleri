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
#Tweepy kütüphanesinden hangi fonksiyonu kullanacaksanız ona göre api değişkeni üzerinden kodlama yapmalısınız.

tweets=api.user_timeline(screen_name="kullaniciadi",count=200) # tweet sayısı maksimum 200 
#istenilen kullacının kullaniciadi girilerek tweetleri çekilebilir.

for tweet in tweets:
    print((tweet.text).encode("utf-8"))