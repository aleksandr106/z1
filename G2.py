def call(g,start,called):
    q=[start]
    called.add(start)
    while q:
        current=q.pop(0)
        for i in g[current]:
            if i not in called:
                called.add(i)
                q.append(i)
                nx.draw_networkx_edges(G,pos,edgelist=[(current,i)],
                       width=8,alpha=0.5,edge_color='r')
def call1(g,start,called1):
    called1.add(start)
    for i in g[start]:
        if i not in called1:
            nx.draw_networkx_edges(G,pos,edgelist=[(start,i)], width=8,alpha=0.5,edge_color='b',style='dashed')
            call1(g,i,called1)
import networkx as nx
import matplotlib.pyplot as plt
n=int(input())
m=int(input())
g={}
for i in range(m):
    a,b= input().split()
    a,b=int(a),int(b)
    if a not in g:
        g[a]={b}
    else:
        g[a].add(b)
    if b not in g:
        g[b]={a}
    else:
        g[b].add(a)
G=nx.Graph(g)
for i in range(1,n+1):
    if i not in g:
        G.add_node(i)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G,pos,node_color='b',node_size=500,alpha=0.8)
nx.draw_networkx_edges(G,pos,alpha=0.7)
nx.draw_networkx_labels(G,pos,font_size=16)
plt.axis('off')
plt.savefig("labels_and_colors.png")
called=set()
called1=set()
call(g,1,called)
call1(g,1,called1)
plt.show() # display




