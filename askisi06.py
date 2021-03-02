import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("","")
auth.set_access_token("","")
def get_tweets():
  client= tweepy.API(auth)
  return client
if __name__ =="__main__":
  user=input("Enter a twitter username: ")
  client=get_tweets()
  for status in tweepy.Cursor(client.home_timeline,screen_name=user).items(10):
   print(status.text)
