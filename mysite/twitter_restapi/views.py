# from __future__ import unicode_literals
from django.shortcuts import render,HttpResponse,redirect,render_to_response
import tweepy
import matplotlib.pyplot as plt
from collections import Counter
import json
from nltk.corpus import stopwords
import string
from os import path
from wordcloud import WordCloud
import json,io
import requests
# from django.utils import simplejson
import json as simplejson
import jsonpickle
import networkx as nx
# import matplotlib.pyplot as plt
# from djanjo.http import HttpResponse,JsonResponse
# from poster.encode import multipart_encode
# from poster.streaminghttp import register_openers
# import urllib2
# Create your views here.
consumer_key="8u9qANlr82Ny1VJczx9zc9viU"
consumer_secret="GLEmFa1XfiV00zKFsLa0ueJa2VnT8HeLgup7awBjfKTbm8oSlc"
access_token="759139555484299264-344z80RdEXKiI57tca0QNEpOkrdtp2K"
access_token_secret="sLGNdpfDoMHxqFMKBNIwAzpI4vu6U1PWX5uS17m9b0mSP"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

def home(request):
	return render(request,"homepage.html",{})
def initial(request):
	# name=request.POST.get("Name")
	return render(request,"initial.html",{})
def initial_occur(request):
	# name=request.POST.get("Name")
	return render(request,"initial_occur.html",{})
def initial_network(request):
	return render(request,'initial_network.html',{})

def index(request):
	Sun=0
	Mon=0
	Tue=0
	Wed=0
	Thu=0
	Fri=0
	Sat=0
	print request.method
	if(request.method=='POST'):
		consumer_key="8u9qANlr82Ny1VJczx9zc9viU"
		consumer_secret="GLEmFa1XfiV00zKFsLa0ueJa2VnT8HeLgup7awBjfKTbm8oSlc"
		access_token="759139555484299264-344z80RdEXKiI57tca0QNEpOkrdtp2K"
		access_token_secret="sLGNdpfDoMHxqFMKBNIwAzpI4vu6U1PWX5uS17m9b0mSP"
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)

		api = tweepy.API(auth)
		name=request.POST.get("Name")
		print name
		public_tweets = api.user_timeline(name,count=3200)
	# print public_tweets
		
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
			
				
				
				# field="/media/graph.png"

# print "Sat="+str(Sat)
# print "Sun="+str(Sun)
# print "Mon="+str(Mon)
# print "Tue="+str(Tue)
# print "Wed="+str(Wed)
# print "Thu="+str(Thu)
# print "Fri="+str(Fri)
		DayOfWeekOfCall = [1,2,3,4,5,6,7]
		DispatchesOnThisWeekday = [Mon, Tue, Wed, Thu,Fri,Sat,Sun]

		LABELS = ["Mon", "Tue", "Wed","Thu","Fri","Sat","Sun"]

		plt.bar(DayOfWeekOfCall, DispatchesOnThisWeekday, align='center')
		plt.xticks(DayOfWeekOfCall, LABELS)
		plt.savefig("/Users/apple/Desktop/Gunkirat/twitter_task/mysite/graph.png")
		plt.clf()

	# return redirect("/twitter/image/")
	return render(request,"index.html",{'Sun':Sun,'Sat':Sat,'Mon':Mon,'Tue':Tue,'Thu':Thu,'Fri':Fri,'Wed':Wed})

def initial_cloud(request):
	return render(request,"initial_cloud.html",{})

def cloud(request):
	
	api = tweepy.API(auth)
	words=[]
	punctuation = list(string.punctuation)
	stop = stopwords.words('english') + punctuation + ['rt', 'via','RT']
	name=request.POST.get("Name")
	public_tweets = api.user_timeline(name)
	counts=dict()
	for tweets in public_tweets:
		jsonfile=tweets.text
	# y=jsonfile.split(" ")
		y=json.dumps(jsonfile)
		y=y[1:-1]
		# y=filter(lambda x:x[0]!="@", y.split())
		# print y
		y=y.split()
		print y
		for i in y:
			# print i
			error=0
			if i not in stop and i[0]!="\\":
				for p in range(len(i)):
					if i[p]=='\\' or i[p]=="/":
						error=error+1	
				if error==0:
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
	# print only_word	
	str1=""

	for l in only_word:
		str1=str1+" "+str(l)
	# print str1


# # Read the whole text.
# # text = open(path.join(d, 'constitution.txt')).read()

# # Generate a word cloud image

	# print str1
	wordcloud = WordCloud().generate(str1)
	plt.figure()
	plt.imshow(wordcloud)
	plt.axis("off")
	plt.savefig("/Users/apple/Desktop/Gunkirat/twitter_task/mysite/cloud.png")
	plt.clf()
	
	return render(request,"cloud.html",{})

def draw_graph(graph1,graph2, graph_layout='spring',
               node_size=1600, node_alpha=0.3,
               node_text_size=12,
               edge_color='black', edge_alpha=0.3, edge_tickness=1,
               edge_text_pos=0.3,
               text_font='sans-serif'):

    # create networkx graph
    G=nx.Graph()
    H=nx.Graph()

    # add edges
    for edge in graph1:
        G.add_edge(edge[0], edge[1])
    for edge in graph2:
        H.add_edge(edge[0], edge[1])    

    # these are different layouts for the network you may try
    # shell seems to work best
    if graph_layout == 'spring':
        graph_pos=nx.spring_layout(G)
    elif graph_layout == 'spectral':
        graph_pos=nx.spectral_layout(G)
    elif graph_layout == 'random':
        graph_pos=nx.random_layout(G)
    else:
        graph_pos=nx.shell_layout(H)
    if graph_layout == 'spring':
        graph_pos=nx.spring_layout(H)
    elif graph_layout == 'spectral':
        graph_pos=nx.spectral_layout(H)
    elif graph_layout == 'random':
        graph_pos=nx.random_layout(H)
    else:
        graph_pos=nx.shell_layout(H)

    # draw graph
    nx.draw_networkx_nodes(G,graph_pos,node_size=node_size, 
                           alpha=node_alpha, node_color="blue")
    nx.draw_networkx_edges(G,graph_pos,width=edge_tickness,
                           alpha=edge_alpha,edge_color=edge_color)
    nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size,
                            font_family=text_font)
    nx.draw_networkx_nodes(H,graph_pos,node_size=node_size, 
                           alpha=node_alpha, node_color="red")
    nx.draw_networkx_edges(H,graph_pos,width=edge_tickness,
                           alpha=edge_alpha,edge_color=edge_color)
    nx.draw_networkx_labels(H, graph_pos,font_size=node_text_size,
                            font_family=text_font)

    # if labels is None:
    #     labels = range(len(graph))

    # edge_labels = dict(zip(graph, labels))
    # nx.draw_networkx_edge_labels(G, graph_pos,
    #                              label_pos=edge_text_pos)

    # show graph
    plt.savefig("/Users/apple/Desktop/Gunkirat/twitter_task/mysite/network.png")
def network(request):
	api = tweepy.API(auth)
# words=[]
# punctuation = list(string.punctuation)
# stop = stopwords.words('english') + punctuation + ['rt', 'via','RT']
# name=request.POST.get("Name")
	new_list=[]
	new_list1=[]
	new_list2=[]
	name_id=""
	search_name="narendramodi"

	public_tweets = api.followers(search_name)
	for tweets in public_tweets:
		jsonfile=tweets._json
		# print jsonfile
		for feed in jsonfile:
			if(feed=='name'):
				name_i=jsonfile[feed]
			# print name
				name_id=name_i.encode("utf-8")
				name=(search_name,name_id)
				new_list.append(name)
				new_list1.append(name)
# print new_list			


	following=api.followers_ids(search_name)
# print following[0]

# user=api.get_user(following[0])
# print user
	for i in range(0,30):
		user=api.get_user(following[i])
		json=user._json
	# print json
		for j in json:
			if(j=='name'):
				name_follow_i=json[j]
				name_id=name_follow_i.encode("utf-8")
				name_follow=(name_id,search_name)
			# print name_follow
				new_list.append(name_follow)
				new_list2.append(name_follow)
	print new_list
	draw_graph(new_list1,new_list2)
	return render(request,"network.html",{})	

