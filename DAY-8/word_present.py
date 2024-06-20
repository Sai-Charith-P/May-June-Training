def solve(i,j,mat,index,n):
    if index>=len(ip):
        return 1
    if i<0 or j<0 or i>=n or j>=n or mat[i][j]!=ip[index]:
        return 0
    return solve(i+1,j,mat,index+1,n) or solve(i,j+1,mat,index+1,n) or solve(i-1,j,mat,index+1,n) or solve(i,j-1,mat,index+1,n)
n=4
mat=[['r','a','q','t'],['a','s','a','v'],['w','e','w','d'],['a','e','w','a']]
ip="set"
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
'''