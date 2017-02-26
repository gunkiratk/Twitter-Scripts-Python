from __future__ import unicode_literals
import tweepy
from collections import Counter
import json
from nltk.corpus import stopwords
import string
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
consumer_key="8u9qANlr82Ny1VJczx9zc9viU"
consumer_secret="GLEmFa1XfiV00zKFsLa0ueJa2VnT8HeLgup7awBjfKTbm8oSlc"
access_token="759139555484299264-344z80RdEXKiI57tca0QNEpOkrdtp2K"
access_token_secret="sLGNdpfDoMHxqFMKBNIwAzpI4vu6U1PWX5uS17m9b0mSP"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
# words={}
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via']

public_tweets = api.user_timeline("narendramodi")
counts=dict()
for tweets in public_tweets:
	jsonfile=tweets.text
	# y=jsonfile.split(" ")
	y=json.dumps(jsonfile)
	y=y[1:-1]
	
	y=y.split()
	# count_all = Counter()
	# print y
	
	for i in y:
		# print i
		# if i not in stop:
		counts[i] = counts.get(i, 0) + 1
	# print counts	
words=sorted(counts.items(), key=lambda x:x[1],reverse=True)
# print words
# print counts
# occurence=count_all.most_common(50)
# print occurence
new_word=[]
for j in range(0,50):
	new_word.append(words[j])

only_word=[]
for k in new_word:
	only_word.append(k[0])
print only_word	
str1=""

for l in new_word:
	str1=str1+" "+str(l)
print str1


# # Read the whole text.
# # text = open(path.join(d, 'constitution.txt')).read()

# # Generate a word cloud image
wordcloud = WordCloud().generate(str1)

# # Display the generated image:
# # the matplotlib way:
# # import matplotlib.pyplot as plt
# # plt.imshow(wordcloud)
# # plt.axis("off")

# # take relative word frequencies into account, lower max_font_size
# # wordcloud = WordCloud(max_font_size=40, relative_scaling=.5).generate(str1)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()


# 	