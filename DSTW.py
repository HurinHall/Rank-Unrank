#     _______________________________________________
#    |Created by Hurin                                       
#    |11/06/2017
#    |Copyright 2017 Iceloof All rights reserved                 
#    |_______________________________________________
#    Dominating Set for Treewidth (COMPSCI 720)

#!/usr/local/bin/python
import re,array

INF=1073741824
unrankArray=[]
static=[]
static1=[]
def rankDS(f,t):
  num=0
  for i in range(t+1):
      num=num*3+f[t-i]
  return num

def unrankDS(num,t):
  f=[]
  for i in range(t+1):
    f.append(num % 3)
    num=int(num/3)
  return f
  
def pwDS(pwTokens,state,t):
  for op in pwTokens:
    op=int(op)
    v1=op%10
    v2=int(op/10)
    stateOld=state[:]
    if op > 9: 
      for i in range(3**(t+1)): 
        f=unrankArray[i]
        if (f[v1]==0 and f[v2]==2) or (f[v1]==2 and f[v2]==0):
            state[i]=INF
        elif f[v1]==0 and f[v2]==1: 
            fnew=f[:]
            fnew[v2]=2
            inew=rankDS(fnew,t)
            state[i]=min(stateOld[i],stateOld[inew])
        elif f[v1]==1 and f[v2]==0:
            fnew=f[:]
            fnew[v1]=2
            inew=rankDS(fnew,t)
            state[i]=min(stateOld[i],stateOld[inew])
    else:          
            for i in range(3**(t+1)): 
                f=unrankArray[i]
                if f[v1]==0: 
                    fnew=f[:]
                    fnew[v1]=1
                    inew=rankDS(fnew,t)
                    state[i]=min(stateOld[i],stateOld[inew])+1
                elif f[v1]==1:
                    state[i]=INF
                elif f[v1]==2: 
                    fn1=f[:]
                    fn1[v1]=0
                    in1=rankDS(fn1,t)
                    fn2=f[:]
                    fn2[v1]=1
                    in2=rankDS(fn2,t)
                    state[i]=min(stateOld[in1],stateOld[in2])
  return state

def init_count(n,t):
  cnt=0
  for j in range(t+1):
    if int(n % 3)==1:
        return INF 
    elif int(n % 3)==0:
        cnt+=1
    n=int(n/3)
  return cnt

def twDS(G,t):
  G=G.strip()
  state=static1[:]
  if len(G)==0:
      return state
  if G[0]!='(':
      return pwDS(re.findall('\d+',G),state,t)
  level=1
  for i in range(1,len(G)): 
    if G[i]==')': level-=1
    elif G[i]=='(': level+=1
    if level==0: 
      state1=twDS(G[1:i-1],t) 
      while 1: 
        k=G[i+1:].find('('); 
        if k==-1:
            return pwDS(re.findall('\d+',G[i+1:]),state1,t)
        for j in range(i+1+k,len(G)): 
          if G[j]==')': level-=1
          elif G[j]=='(': level+=1
          if level==0: 
            state2=twDS(G[i+2+k:j-1],t); 
            state=static[:]
            for x in range(3**(t+1)): 
              for y in range(3**(t+1)): 
                f1=unrankArray[x]
                f2=unrankArray[y]
                f=[]
                common=0
                for z in range(t+1):  
                   if f1[z]==0 and f2[z]==0:
                       common+=1
                   if f1[z]==0 or f2[z]==0:
                       f.append(0) 
                   elif f1[z]==2 and f2[z]==2:
                       f.append(2)
                   else:
                       f.append(1)
                r=rankDS(f,t)
                s1=state1[rankDS(f1,t)]
                s2=state2[rankDS(f2,t)]
                if s1<INF and s2<INF:
                    state[r]=min(state[r],s1+s2-common)
            if j+1 < len(G): 
              state1=state
              i=j+1 
              break  
            else:
                return state

while True:
    s=input("")              
    i=s.find('(')
    t=int(s[0:i-1])
    s=s[i:] 
    best=INF
    unrankArray=[]
    for i in range(3**(t+1)):
      unrankArray.append(unrankDS(i,t))
    static=array.array('i', map((lambda n:INF), range(3**(t+1))))
    static1=array.array('i', map((lambda n:init_count(n,t)), range(3**(t+1))))
    state=twDS(s,t)
    for i in range(3**(t+1)): 
      flag=1
      for f in unrankArray[i]: 
        if f==2:
            flag=0
            break
      if flag:
          best = min(best,state[i])
    print(best)
    if t == 0:
        break
