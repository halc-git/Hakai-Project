from collections import defaultdict

N,M=map(int,input().split())
A=[]
for i in range(N):
    A.append(list(input()))
bomb=[]
for i in range(M):
    C,L=map(int,input().split())
    bomb.append([C,[]])
    for j in range(L):
        bomb[-1][-1].append(tuple(map(int,input().split())))
Q=int(input())
assert 0<=Q<=100000
py=0
px=0
bought=defaultdict(int)
cnt=0
cost=0
for i in range(Q):
    t,x=input().split()
    if t=="1":
        if x=="L":
            px-=1
        elif x=="R":
            px+=1
        elif x=="U":
            py-=1
        elif x=="D":
            py+=1
        else:
            assert False
        assert 0<=px<N and 0<=py<N
        if A[py][px]==".":
            cost+=(cnt+1)**2
        else:
            cost+=2*((cnt+1)**2)
    elif t=="2":
        x=int(x)
        assert 1<=x<=M
        assert A[py][px]=="@"
        bought[x]+=1
        cnt+=1
        cost+=bomb[x-1][0]
    elif t=="3":
        x=int(x)
        assert bought[x]>0
        for by,bx in bomb[x-1][1]:
            if 0<=px+bx<N and 0<=py+by<N:
                A[py+by][px+bx]="."
        bought[x]-=1
        cnt-=1
    else:
        assert False
ok=1
for i in range(N):
    for j in range(N):
        if A[i][j]!=".":
            ok=0
score=0
if ok==0:
    score=1
else:
    score=max(10,1000000000000/(1000000+cost))
print("score:"+str(int(score))+"(cost:"+str(cost)+")")
