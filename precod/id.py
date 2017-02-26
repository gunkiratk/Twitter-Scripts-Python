import tweepy
import networkx as nx
# import matplot
import networkx as nx
import matplotlib.pyplot as plt
# import networkx as nx
# import matplotlib.pyplot as plt
import sys
# def draw_graph(graph):

#     # extract nodes from graph
#     nodes = set([n1 for n1, n2 in graph] + [n2 for n1, n2 in graph])

#     # create networkx graph
#     G=nx.Graph()

#     # add nodes
#     for node in nodes:
#         G.add_node(node)

#     # add edges
#     for edge in graph:
#         G.add_edge(edge[0], edge[1])

#     # draw graph
#     pos = nx.shell_layout(G)
#     nx.draw(G, pos)

#     # show graph
#     plt.show()

# draw example

consumer_key="8u9qANlr82Ny1VJczx9zc9viU"
consumer_secret="GLEmFa1XfiV00zKFsLa0ueJa2VnT8HeLgup7awBjfKTbm8oSlc"
access_token="759139555484299264-344z80RdEXKiI57tca0QNEpOkrdtp2K"
access_token_secret="sLGNdpfDoMHxqFMKBNIwAzpI4vu6U1PWX5uS17m9b0mSP"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

def draw_graph(graph1,graph2, graph_layout='spring',
               node_size=1000, node_alpha=0.3,
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

    plt.show()

api = tweepy.API(auth)
# words=[]
# punctuation = list(string.punctuation)
# stop = stopwords.words('english') + punctuation + ['rt', 'via','RT']
# name=request.POST.get("Name")
new_list=[]
new_list1=[]
new_list2=[]
name_id=""
search_name=sys.argv[1]

public_tweets = api.followers(search_name)
for tweets in public_tweets:
	jsonfile=tweets._json
	# print jsonfile
	for feed in jsonfile:
		if(feed=='name'):
			name_i=jsonfile[feed]
			# print name
			name_id=name_i.encode("utf-8")
			# name_id.set_xlabel
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