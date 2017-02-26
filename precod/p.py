import tweepy
import plotly.plotly as py
import plotly.graph_objs as go
consumer_key="8u9qANlr82Ny1VJczx9zc9viU"
consumer_secret="GLEmFa1XfiV00zKFsLa0ueJa2VnT8HeLgup7awBjfKTbm8oSlc"
access_token="759139555484299264-344z80RdEXKiI57tca0QNEpOkrdtp2K"
access_token_secret="sLGNdpfDoMHxqFMKBNIwAzpI4vu6U1PWX5uS17m9b0mSP"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.user_timeline("narendramodi",count=3200)
# print public_tweets
Sun=0
Mon=0
Tue=0
Wed=0
Thu=0
Fri=0
Sat=0
for tweet in public_tweets:
    jsonfile=tweet._json
    for feed in jsonfile:
    	if(feed=='created_at'):
 			# print jsonfile[feed]
 			day=jsonfile[feed].split(' ',1)[0]
 			# print day
 			if(day=='Sun'):
 				Sun=Sun+1
 			if(day=='Mon'):
 				Mon=Mon+1
 			if(day=='Tue'):
 				Tue=Tue+1
 			if(day=='Wed'):
 				Wed=Wed+1
 			if(day=='Thu'):
 				Thu=Thu+1
 			if(day=='Fri'):
 				Fri=Fri+1
 			if(day=='Sat'):
 				Sat=Sat+1			

print "Sat="+str(Sat)
print "Sun="+str(Sun)
print "Mon="+str(Mon)
print "Tue="+str(Tue)
print "Wed="+str(Wed)
print "Thu="+str(Thu)
print "Fri="+str(Fri)


data = [go.Bar(
            x=['Sun','Mon','Tue','Wed','Thu','Fri','Sat'],
            y=[Sun, Mon, Tue,Wed,Thu,Fri,Sat]
    )]

py.iplot(data, filename='basic-bar')

