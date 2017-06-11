#     _______________________________________________
#    |Created by Hurin                                       
#    |11/06/2017
#    |Copyright 2017 Iceloof All rights reserved                 
#    |_______________________________________________
#    Dominating Set for Pathwidth (COMPSCI 720)

#!/usr/local/bin/python
import array

INF=1073741824
unrankArray=[]
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

while True:
    s=input()              
    i=s.find('(')
    t=int(s[0:i-1])
    s=s[i:] 
    best=INF
    unrankArray=[]
    for i in range(3**(t+1)):
      unrankArray.append(unrankDS(i,t))
    state1=array.array('i', map((lambda n:init_count(n,t)), range(3**(t+1))))
    state=pwDS([int(x) for x in s.replace("(","").replace(")","").split()],state1,t)
    for i in range(3**(t+1)):
      flag=1
      for f in unrankDS(i,t):
        if f==2:
            flag=0
            break	
      if flag: 
        best = min(best,state[i])
    print(best)
    if t == 0:
        break

