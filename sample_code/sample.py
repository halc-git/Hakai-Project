N,M=map(int,input().split())
A=[]
for i in range(N):
    A.append(input())
bomb=[]
for i in range(M):
    C,L=map(int,input().split())
    bomb.append([C,[]])
    for j in range(L):
        bomb[-1][-1].append(tuple(map(int,input().split())))
x=-1
y=-1
for i in range(N):
    for j in range(N):
        if A[i][j]=="@":
            x=i
            y=j
            break
    if x!=-1:
        break
ans=[]
for i in range(x):
    ans.append([1,"D"])
for i in range(y):
    ans.append([1,"R"])
for i in range(N*N):
    ans.append([2,1])
for i in range(x):
    ans.append([1,"U"])
for i in range(y):
    ans.append([1,"L"])
for i in range(N):
    for j in range(N):
        ans.append([3,1])
        if j==N-1 and i==N-1:
        	break
        if j==N-1:
            ans.append([1,"D"])
        elif i%2==0:
            ans.append([1,"R"])
        else:
            ans.append([1,"L"])
print(len(ans))
for i in ans:
    print(*i)
