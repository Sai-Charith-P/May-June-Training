def solve(i,j,mat):
    if i<0 or j<0 or i>=n or j>=n or mat[i][j]==0:
        return
    if mat[i][j]==1:
        mat[i][j]=0
    solve(i-1,j,mat)
    solve(i,j+1,mat)
    solve(i,j-1,mat)
    solve(i+1,j,mat)
n=6
mat=[[0,1,1,1,0,1],[0,1,0,1,0,0],[1,0,1,1,0,0],[0,0,0,1,1,1],[1,1,0,0,0,1],[1,1,1,0,1,0]]
i,j=4,6
solve(i-1,j-1,mat)
print(mat)
count=0
for i in mat:
    for j in i:
        if j==1:
            count+=1
print(count)
'''
i<0,j<0,i>=n,j>=n 
                (i-1,j)
                        
    (i,j-1)        (i,j)       (i,j+1)
                
                (i+1,j)
                
'''