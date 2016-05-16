def dekstra(g,start):
    sp={vertex : float('inf') for vertex in g }
    sp[start]=0
    q=[start]
    while q:
        current=q.pop(0)
        for i in g[current]:
            osp=sp[current]+g[current][i]
            if osp<sp[i]:
                sp[i]=osp
                q.append(i)
    return sp
n=int(input())
m=int(input())
k=int(input())
g={}
for i in range(m):
    s=input().split()
    a=int(s[0])
    b=int(s[1])
    w=float(s[2])
    if a not in g:
        g[a]={b:w}
    else:
        g[a][b]=w
    if b not in g:
        g[b]={a:w}
    else:
        g[b][a]=w
sp=dekstra(g,k)
for vertex in g:
    print(vertex,sp[vertex])




