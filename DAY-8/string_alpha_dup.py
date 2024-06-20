'''s=input()   #abfgresagtyuiofde
ma=0
st=""
for i in range(len(s)):
    st=st+s[i]
    for j in range(i+1,len(s)):
        if s[j] not in st:
            st=st+s[j]
        else:
            break
    if len(st)>ma:
        ma=len(st)
    st=""
print(ma)'''
''' #Using Sliding Window
from collections import defaultdict
s=input()
mp=defaultdict(int)
i=0
j=0
res=0
while j<len(s):
    mp[s[j]]+=1 
    while mp[s[j]]>1:
        mp[s[i]]-=1 
        i+=1 
    print(s[i:j])
    res=max(res,j-i+1)
    j+=1 
print(res)'''
#to reduce the number of loops
s=input()
d={}
res=""
i=0
ma=0
while(i<len(s)):
    while(i<len(s)):
        if(s[i] not in res):
            res=res+s[i]
            d[res[i]]=i 
        else:
            if len(res)>ma:
                ma=len(res)
            res=""
            break
        i+=1
    i=d[s[i]]+1
print(ma)