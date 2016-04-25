input1=open('input1','r')
input2=open('input6','r')
a=['B']*20
c=input1.read(1)
i=0
while len(c)>0:
    a[len(a)//2+i]=c
    i+=1
    c=input1.read(1)
sostoynie=input2.readline().rstrip()
c=input2.readline()
rule=[]
i=0
while len(c)>0:
    c=c.rstrip()
    b=c.split('->')
    rule.append(['']*5)
    rule[i][0]=b[0][0]
    rule[i][1]=b[0][1:]
    if b[1][-1]=='R' or b[1][-1]=='L':
         rule[i][2]=b[1][0]
         rule[i][3]=b[1][1:-1]
         rule[i][4]=b[1][-1]
    else:
         rule[i][2]=b[1][0]
         rule[i][3]=b[1][1:]
    print(rule[i])
    i+=1
    c=input2.readline()

i=len(a)//2
while sostoynie!='STOP':
    for  j  in range  (len(rule)):
        if a[i]==rule[j][0] and sostoynie==rule[j][1]:
            k=rule[j]
    a[i]=k[2]
    sostoynie=k[3]
    if k[4]=='R':
        i+=1
    else:
        i-=1
s=''
for i in range(len(a)):
    if a[i]!='B':
        s+=a[i]
print(s)












