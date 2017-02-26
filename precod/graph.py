# from __future__ import unicode_literals
import tweepy
from collections import Counter
import json
from nltk.corpus import stopwords
import string
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import json,io
import networkx as nx
import matplotlib.pyplot as plt
import sys

consumer_key="8u9qANlr82Ny1VJczx9zc9viU"
consumer_secret="GLEmFa1XfiV00zKFsLa0ueJa2VnT8HeLgup7awBjfKTbm8oSlc"
access_token="759139555484299264-344z80RdEXKiI57tca0QNEpOkrdtp2K"
access_token_secret="sLGNdpfDoMHxqFMKBNIwAzpI4vu6U1PWX5uS17m9b0mSP"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

def draw_graph(graph, labels=None, graph_layout='shell',
               node_size=1600, node_color='blue', node_alpha=0.3,
               node_text_size=12,
               edge_color='blue', edge_alpha=0.3, edge_tickness=1,
               edge_text_pos=0.3,
               text_font='sans-serif'):

    # create networkx graph
    G=nx.Graph()

    # add edges
    for edge in graph:
        G.add_edge(edge[0], edge[1])

    # these are different layouts for the network you may try
    # shell seems to work best
    # if graph_layout == 'spring':
    #     print 1
    #     graph_pos=nx.spring_layout(G)
    # elif graph_layout == 'spectral':
    #     print 2
    #     graph_pos=nx.spectral_layout(G)
    # elif graph_layout == 'random':
    #     print 3
    #     graph_pos=nx.random_layout(G)
    # else:
        # print 4
        graph_pos=nx.shell_layout(G)

    # draw graph
    nx.draw_networkx_nodes(G,graph_pos,node_size=node_size, 
                           alpha=node_alpha, node_color=node_color)
    nx.draw_networkx_edges(G,graph_pos,width=edge_tickness,
                           alpha=edge_alpha,edge_color=edge_color)
    nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size,
                            font_family=text_font)

    if labels is None:
        labels = range(len(graph))

    edge_labels = dict(zip(graph, labels))
    nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels, 
                                 label_pos=edge_text_pos)

    # show graph
    plt.show()

# graph = [('people', 'better.'), ('campaign.', '@nstomar:'), ('@swachhbharat', '@nstomar:'), ('give', 'best'), ('@nstomar:', '@swachhbharat'), ('covered', '#MannKiBaat'), ('@SwachhBharat', 'Gramin'), ('Urged', 'officers'), ('125', 'My'), ('Gramin', 'August')]
api = tweepy.API(auth)
words=[]
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via','RT']
# name=request.POST.get("Name")
public_tweets = api.user_timeline(sys.argv[1])
counts=dict()
new_list=[]
for tweets in public_tweets:
    jsonfile=tweets.text
    # y=jsonfile.split(" ")
    y=json.dumps(jsonfile)
    y=y[1:-1]
        # y=filter(lambda x:x[0]!="@", y.split())
        # print y
    y=y.split()
    # print y

    for i in y:
            # print i
        
        error=0
        if i not in stop and i[0]!="\\":
            for p in range(len(i)):
                if i[p]=='\\' or i[p]=="/":
                    error=error+1   
            if error==0:
                new_list.append(i)  
                counts[i] = counts.get(i, 0) + 1
    # print counts
words=sorted(counts.items(), key=lambda x:x[1],reverse=True)
# print words
# print counts
# occurence=count_all.most_common(50)
# print occurence
new_word=[]
for j in range(0,30):
        new_word.append(words[j])

only_word=[]
for k in new_word:
    only_word.append(k[0])
# print only_word   


new_dict=dict()
for i in only_word:
    new_dict[i]=dict()
for i in new_dict:
    for j in only_word:
        new_dict[i][j]=0;   
# print new_dict
# print new_list
for key in new_dict:
    # print key
    for i in new_list:
#   #   jsonfile=tweets.text
#   # # y=jsonfile.split(" ")
#   #   y=json.dumps(jsonfile)
#   #   y=y[1:-1]
#   #   y=y.split()
        if i==key:
            # print i
            # print new_list[new_list.index(i)+1]
            for j in only_word:
                if new_list[new_list.index(i)+1]==j:
                    # print new_list[new_list.index(i)+1]
                    new_dict[key][new_list[new_list.index(i)+1]]=new_dict[key][new_list[new_list.index(i)+1]]+1

# you may name your edge labels
graph=[]
labels=[]
for key in new_dict:
    for i in new_dict[key]:
        if new_dict[key][i]!=0:
            link=(key,i)
            graph.append(link)
            labels.append(new_dict[key][i])

# if edge labels is not specified, numeric labels (0, 1, 2...) will be used
draw_graph(graph,labels)