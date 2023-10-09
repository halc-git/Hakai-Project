import pygame
import sys
from collections import defaultdict
from copy import deepcopy

def main():
    input_file=open("./visualizer/in.txt","r")
    N,M=map(int,input_file.readline().split())
    A=[]
    for i in range(N):
        A.append(list(input_file.readline())[:-1])
    bomb=[]
    for i in range(M):
        C,L=map(int,input_file.readline().split())
        bomb.append([C,[]])
        for j in range(L):
            bomb[-1][-1].append(tuple(map(int,input_file.readline().split())))
    input_file.close()
    std_input=open("./visualizer/out.txt","r")
    Q=int(std_input.readline())
    assert 0<=Q<=100000
    py=0
    px=0
    bought=defaultdict(int)
    cnt=0
    cost=0
    query=[]
    backet=[[deepcopy(A),deepcopy(bought),px,py,cnt,cost]]
    size=100
    for i in range(Q):
        t,x=std_input.readline().split()
        query.append((t,x))
        for j in range(N):
            for k in range(N):
                if A[j][k]=="%":
                    A[j][k]="."
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
                    A[py+by][px+bx]="%"
            bought[x]-=1
            cnt-=1
        else:
            assert False
        if i%size==size-1:
            backet.append([deepcopy(A),deepcopy(bought),px,py,cnt,cost])
    std_input.close()
    pygame.init()
    pygame.display.set_caption("Hakai-Project visualizer")
    high=950
    screen=pygame.display.set_mode((765,high))
    clock=pygame.time.Clock()
    font=pygame.font.Font(None,40)
    turn=0
    speed=1
    pause=0
    bef=pygame.key.get_pressed()
    while True:
        key=pygame.key.get_pressed()
        turn+=pause
        turn%=Q+1
        if turn==Q:
            pause=0
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0,0,0))
        A,bought,px,py,cnt,cost=backet[turn//size]
        A=deepcopy(A)
        bought=deepcopy(bought)
        for i in range(turn%size):
            t,x=query[(turn//size)*size+i]
            for j in range(N):
                for k in range(N):
                    if A[j][k]=="%":
                        A[j][k]="."
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
                        A[py+by][px+bx]="%"
                bought[x]-=1
                cnt-=1
            else:
                assert False
            if i%size==size-1:
                backet.append([deepcopy(A),deepcopy(bought),px,py,cnt,cost])
        ok=1
        for i in range(N):
            for j in range(N):
                if A[i][j]==".":
                    pygame.draw.rect(screen,(115,78,48),[7.5+j*15,(high-765)+7.5+i*15,15,15])
                elif A[i][j]=="#":
                    ok=0
                    pygame.draw.rect(screen,(100,100,100),[7.5+j*15,(high-765)+7.5+i*15,15,15])
                elif A[i][j]=="@":
                    ok=0
                    pygame.draw.rect(screen,(162,96,191),[7.5+j*15,(high-765)+7.5+i*15,15,15])
                else:
                    pygame.draw.rect(screen,(255,0,0),[7.5+j*15,(high-765)+7.5+i*15,15,15])
        for i in range(M):
            now=bought[i+1]/30
            red=max(0,min(255,(now-1/2)*4*255))
            green=max(0,min(255,(1/2-abs(1/2-now))*4*255))
            blue=max(0,min(255,(1/2-now)*4*255))
            pygame.draw.rect(screen,(red,green,blue),[8.75+i*37.5,(high-765)-10-50*min(now,1),35,5+50*min(now,1)])
        pygame.draw.rect(screen,(253,126,0),[11+px*15,(high-765)+11+py*15,8,8])
        txt=font.render("turn:"+str(turn),True,(255,255,255))
        screen.blit(txt,[10,(high-765)-100])
        txt=font.render("cost:"+str(cost),True,(255,255,255))
        screen.blit(txt,[180,(high-765)-100])
        score=1
        if ok:
            score=int(max(10,1000000000000/(10000+cost)))
        txt=font.render("score:"+str(score),True,(255,255,255))
        screen.blit(txt,[450,(high-765)-100])
        if bef[pygame.K_s] and not(key[pygame.K_s]):
            speed=(speed+1)%3
        if bef[pygame.K_p] and not(key[pygame.K_p]):
            pause=1-pause
        if bef[pygame.K_LEFT] and not(key[pygame.K_LEFT]):
            turn=(turn-1)%Q
        if bef[pygame.K_RIGHT] and not(key[pygame.K_RIGHT]):
            turn=(turn+1)%Q
        txt=font.render(["Low","Medium","Fast"][speed],True,(255,255,255))
        screen.blit(txt,[100,(high-765)-140])
        txt=font.render(["Pause","Play"][pause],True,(255,255,255))
        screen.blit(txt,[10,(high-765)-140])
        bef=deepcopy(key)
        pygame.display.update()
        if speed==0:
            clock.tick(10)
        elif speed==1:
            clock.tick(20)
        else:
            clock.tick(50)

if __name__=="__main__":
    main()
