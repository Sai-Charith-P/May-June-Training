def solve(i,j,mat,index,n):
    if index>=len(ip):
        return 1
    if i<0 or j<0 or i>=n or j>=n or mat[i][j]!=ip[index]:
        return 0
    temp=mat[i][j]
    mat[i][j]='.'
    return solve(i+1,j,mat,index+1,n) or solve(i,j+1,mat,index+1,n) or solve(i-1,j,mat,index+1,n) or solve(i,j-1,mat,index+1,n)
    mat[i][j]=temp
n=4
mat=[['r','a','q','t'],['a','b','o','v'],['w','o','o','d'],['a','e','k','a']]
ip="boook"
f=1
for i in range(n):
    for j in range(n):
        if ip[0]==mat[i][j]:
            if solve(i,j,mat,0,n):
                f=0
                print("YES")
                break
if f==1:
    print("NO")
'''
ip:
n=4
r a q t
a s a v
w e w d 
a e w a 
ip="saw"
op:
YES

n=4
r a q t 
a b o v 
w o o d 
a e k a 
ip="book"
op:
NO
'''

def fun(i,j,k,t):
    if(k==len(s)):
        return 1 
    if i<0 or j<0 or i>=n or j >=n or mat[i][j]!=s[k]:
        return
    if(mat[i][j]==s[k]):
        mat[i][j]=0
        if(t!=1):
            t=fun(i+1,j,k+1)
            t=fun(i-1,j,k+1)
            t=fun(i,j-1,k+1)
            t=fun(i,j+1,k+1)
            return t
for i in range(n):
    for j in range(n):
        if(a[i][j]==s[0]):
            c=fun(i,j,1,0)
            if c==1:
                print("YES")
                break
if(c==0):
    print("NO")
    
    '''
    r a q t
    a b o v 
    f o o k 
    l k p d