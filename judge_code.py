import sys
from collections import defaultdict

input_file=open(sys.argv[1],mode='r',encoding='utf-8')
score_file=open(sys.argv[4],mode='w',encoding='utf-8')

std_input=open(0)
N,M=map(int,input_file.readline().split())
A=[]
for i in range(N):
    A.append(list(input_file.readline()))
bomb=[]
for i in range(M):
    C,L=map(int,input_file.readline().split())
    bomb.append([C,[]])
    for j in range(L):
        bomb[-1][-1].append(tuple(map(int,input_file.readline().split())))

Q=int(std_input.readline())
assert 0<=Q<=100000
py=0
px=0
bought=defaultdict(int)
cnt=0
cost=0
for i in range(Q):
    t,x=std_input.readline().split()
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
last=std_input.readline()
assert last==""
ok=1
for i in range(N):
    for j in range(N):
        if A[i][j]!=".":
            ok=0
score=0
if ok==0:
    score=1
else:
    score=max(10,1000000000000/(10000+cost))
print(int(score),file=score_file)
input_file.close()
score_file.close()
