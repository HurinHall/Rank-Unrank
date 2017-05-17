#     _______________________________________________
#    |Created by Hurin                                       
#    |09/05/2017
#    |Copyright 2017 Iceloof All rights reserved                 
#    |_______________________________________________
#    Rank and Unrank for lex order(integer partitions)

def p(n,k):
    if k==1 or n<1: return 0
    elif k==2: return 1
    elif k>n: return p(n,n)+1
    else: return p(n,k-1)+p(n-(k-1),k)


print ('Please choose')
print ('1. Ranking')
print ('2. Unranking')
choice = int(input('Your choice: '))
if choice == 1:
    order = input('Please input permutation(space between number): ')
    item = order.split()
    n = 0
    tmp = 0
    for i in range(len(item)):
        n += int(item[i])
    rank = p(n,n+1)
    print("P(",n,")=",rank)
    for i in range(len(item)):
        n = n - tmp
        rank -= p(n,int(item[i]))
        print("P(",n,",",item[i],")=",p(n,int(item[i])))
        tmp = int(item[i])
    rank -= 1
    print (rank)
elif choice == 2:
    n = int(input('Input n: '))
    rank = int(input('Input rank: '))
    rank = p(n,n+1) - rank -1
    result = []
    # Dynamic Programming may be better
    while True:
        i = n
        while p(n,i) > rank:
            i -= 1
        result.append(i),
        rank = rank - p(n,i)
        n -= i
        if n == 0:
            break
    print(result)
else:
    print("Error")
