from collections import defaultdict
s=input()
'''alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
c=0
for i in s:
    if i in alp:
        c=1
    else:
        c=0
if c==1:
    print("YES")
else:
    print("NO")'''
'''s1=set(s)
if(len(s1)==27):
    print("YES")
else:
    print("NO")'''     #the quick brown fox jumps over the lazy dog
    
'''
mp=defaultdict(int)
for i in s:
    if i.isalpha() and i.islower():     #the 4quick br$own fo%x jumps o.ver the lazy dog
        mp[i]+=1 
if len(mp.keys())==26:
    print("YES")
else:
    print("NO")
'''
'''
for i in range(97,123):
    if(chr(i) not in s):
        print("NO")
        break
else:
    print("YES")'''
    
'''d={}
for i in s:
    if(i.islower()):
        d[i]=1
print(d)
if(len(d)==26):
    print("YES")
else:
    print("NO")'''
    
d=[0]*26
for i in s:
    if(i.islower()):
        d[ord(i)-97]+=1 
print(all(d))
