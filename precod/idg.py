import plotly.plotly as py
from plotly.graph_objs import *

import networkx as nx

G=nx.random_geometric_graph(200,0.125)
pos=nx.get_node_attributes(G,'pos')

dmin=1
ncenter=0
for n in pos:
    x,y=pos[n]
    d=(x-0.5)**2+(y-0.5)**2
    if d<dmin:
        ncenter=n
        dmin=d
        
p=nx.single_source_shortest_path_length(G,ncenter)
edge_trace = Scatter(
    x=[], 
    y=[], 
    line=Line(width=0.5,color='#888'),
    hoverinfo='none',
    mode='lines')

for edge in G.edges():
    x0, y0 = G.node[edge[0]]['pos']
    x1, y1 = G.node[edge[1]]['pos']
    edge_trace['x'] += [x0, x1, None]
    edge_trace['y'] += [y0, y1, None]

node_trace = Scatter(
    x=[], 
    y=[], 
    text=[],
    mode='markers', 
    hoverinfo='text',
    marker=Marker(
        showscale=True,
        # colorscale options
        # 'Greys' | 'Greens' | 'Bluered' | 'Hot' | 'Picnic' | 'Portland' |
        # Jet' | 'RdBu' | 'Blackbody' | 'Earth' | 'Electric' | 'YIOrRd' | 'YIGnBu'
        colorscale='YIGnBu',
        reversescale=True,
        color=[], 
        size=10,         
        colorbar=dict(
            thickness=15,
            title='Node Connections',
            xanchor='left',
            titleside='right'
        ),
        line=dict(width=2)))

for node in G.nodes():
    x, y = G.node[node]['pos']
    node_trace['x'].append(x)
    node_trace['y'].append(y)
for node, adjacencies in enumerate(G.adjacency_list()):
    node_trace['marker']['color'].append(len(adjacencies))
    node_info = '# of connections: '+str(len(adjacencies))
    node_trace['text'].append(node_info)
fig = Figure(data=Data([edge_trace, node_trace]),
             layout=Layout(
                title='<br>Network graph made with Python',
                titlefont=dict(size=16),
                showlegend=False, 
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                annotations=[ dict(
                    text=[('narendramodi', 'Oloniyo Flourish'), ('narendramodi', 'Fares'), ('narendramodi', 'Nawab Hundal'), ('narendramodi', 'Zahir shah'), ('narendramodi', 'Durgesh kushawaha'), ('narendramodi', 'shivangi pandey'), ('narendramodi', 'narendarkumarnirmal'), ('narendramodi', 'AJAY KUMAR SAHU'), ('narendramodi', 'Imtiyaz Hannan'), ('narendramodi', 'ColorFizz'), ('narendramodi', 'Dilip Sidhani'), ('narendramodi', 'Girish GG'), ('narendramodi', 'Dashmeet Singh'), ('narendramodi', 'BIAFRA 3.5M GENOCIDE'), ('narendramodi', 'Pradeep Singh'), ('narendramodi', 'Bilge Tanyeri'), ('narendramodi', 'Komen King'), ('narendramodi', 'SHANU CHAUHAN'), ('narendramodi', 'Akash Kumar'), ('narendramodi', 'Lakshay Gulati'), ('Oloniyo Flourish', 'narendramodi'), ('Fares', 'narendramodi'), ('Nawab Hundal', 'narendramodi'), ('Zahir shah', 'narendramodi'), ('Durgesh kushawaha', 'narendramodi'), ('shivangi pandey', 'narendramodi'), ('narendarkumarnirmal', 'narendramodi'), ('AJAY KUMAR SAHU', 'narendramodi'), ('Imtiyaz Hannan', 'narendramodi'), ('ColorFizz', 'narendramodi'), ('Dilip Sidhani', 'narendramodi'), ('Girish GG', 'narendramodi'), ('Dashmeet Singh', 'narendramodi'), ('BIAFRA 3.5M GENOCIDE', 'narendramodi'), ('Pradeep Singh', 'narendramodi'), ('Bilge Tanyeri', 'narendramodi'), ('Komen King', 'narendramodi'), ('SHANU CHAUHAN', 'narendramodi'), ('Akash Kumar', 'narendramodi'), ('Lakshay Gulati', 'narendramodi'), ('Jafet', 'narendramodi')],
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.005, y=-0.002 ) ],
                xaxis=XAxis(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=YAxis(showgrid=False, zeroline=False, showticklabels=False)))

py.iplot(fig, filename='networkx')

