import networkx as nx
import matplotlib.pyplot as plt
n=int(input())
m=int(input())
g={}
for i in range(m):
    a,b,w= input().split()
    a,b,w=int(a),int(b),float(w)
    if a not in g:
        g[a]={b:{'weight':w}}
    else:
        g[a][b]={'weight':w}
    if b not in g:
        g[b]={a:{'weight':w}}
    else:
        g[b][a]={'weight':w}
G=nx.Graph(g)
pos=nx.spring_layout(G)

nx.draw_networkx_nodes(G,pos,node_color='b',node_size=500,alpha=0.8)

nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)
nx.draw_networkx_edges(G,pos,width=8,alpha=0.5,edge_color='r')
nx.draw_networkx_labels(G,pos,font_size=16)

plt.axis('off')
plt.savefig("labels_and_colors.png")
plt.show() # display