#ip: [1,2,3,4,1,2,3,1,2] op: [[1 2 3 4],[1 2 3],[1 2]]
'''l=list(map(int,input().split()))
res=[]
old=[]
for i in l:
    if i not in old:
        old.append(i)
    else:
        res.append(old)
        old=[i]
res.append(old)
print(res)'''
#ip:[2,3,1,3,4,3,2]  op:[[2 3 1 4],[3 2],[3]]  ip:[4,5,2,1]  op:[[4,5,2,1]]
'''from collections import Counter
l=list(map(int,input().split()))
mp=Counter(l)
res=[]
count=0                                 #[2,3,1,3,4,2,3]
while True:                             #{2:2,3:3,1:1,4:1}
    out=[]                              #{2:1,3:2,1:0,4:0}
    for i in mp:                        #{2:0,3:1,1:0,4:0}
        if mp[i]:
            count+=1
            out.append(i)               #using counter dictionaries
            mp[i]-=1
    res.append(out)
    if count==len(l):
        break
print(res)'''
'''l=list(map(int,input().split()))
m=[]
c=0
while(c!=len(l)):
    r=[]
    for i in range(len(l)):         
        if(not str(l[i]).isalpha()):
            if(l[i] not in r):
                c+=1
                r.append(l[i])
                l[i]='a'            #change numbers to alphabets once seen
    m.append(r)
print(m)'''
'''l=list(map(int,input().split()))
d={}
m=[]
c=0
for i in l:         
    if(i not in d):
        d[i]=1
    else:
        d[i]=s[i]+1
c=0
while(c!=len(l)):
    r=[]
    for i in d:
        '''