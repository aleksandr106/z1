def call(g,start,called):
    q=[start]
    called.add(start)
    while q:
        current=q.pop(0)
        if current in g:
            for i in g[current]:
                if i not in called:
                   called.add(i)
                   q.append(i)
def cal1(g,start,called1):
    called1.add(start)
    for i in g(start):
        if i not in called1:
            call(g,i,called1)
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
called=set()
called1=set()
call(g,1,called)
call(g,1,called1)
if len(called)==n:
    print('Связный граф')
    print('Компенента связности', called)
else:
    print('Несвязный граф')
    t=1
    print('1 Компенента связности', called)
    for j in range(1,n+1):
        if j not in called:
            called1=set()
            call(g,int(j),called1)
            called.update(called1)
            t+=1
            print(t,'Компенента связности', called1)
