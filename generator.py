import random

N=50
M=20
print(N,M)
A=[["." for i in range(N)] for i in range(N)]
c=random.random()*0.3+0.5
for i in range(N):
    for j in range(N):
        if random.random()<c:
            A[i][j]="#"
s=max(10,int(random.gauss(50,10)))
change={random.randint(0,N*N-1) for i in range(s)}
while len(change)<s:
    change={random.randint(0,N*N-1) for i in range(s)}
cnt=0
for i in range(N):
    for j in range(N):
        if cnt in change:
            A[i][j]="@"
        cnt+=1
for i in A:
    print("".join(i))
for i in range(M):
    pos=[]
    s=random.random()*0.8+0.2
    for j in range(-20,21):
        for k in range(-20,21):
            if random.random()<1/(max(abs(j),abs(k))*s+1):
                pos.append((j,k))
    L=len(pos)
    C=int(max(1,min(4000,L*random.gauss(1,0.2))))
    pos.sort(key=lambda x:abs(x[0])+abs(x[1]))
    print(C,L)
    for j in pos:
        print(*j)
