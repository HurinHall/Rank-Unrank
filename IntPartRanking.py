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
    for i in range(len(item)):
        n += int(item[i])
    rank = p(n,n+1)
    print("n=",(n),[p(n,k+1) for k in range(n+2)])
    for i in range(len(item)):
        rank -= p(n,int(item[i]))
    rank -= 1
    print (rank)
elif choice == 2:
    n = int(input('Input n: '))
    rank = int(input('Input rank: '))
    remain = p(n,n+1) - rank -1
    rank = remain
    first = n
    tmp = n
    sum_val = 0
    flag = 0
    result = []
    # Dynamic Programming may be better
    while True:
        p_value = p(n,tmp)
        if rank == p_value:
            if sum_val + tmp == n:
                result.append(tmp)
                print(result)
                break
            elif sum_val + tmp < n and (p_value == 1 or p_value == 0):
                rank = rank - p_value
                sum_val += tmp
                result.append(tmp)
            else:
                tmp = first - 1
                first = tmp
                sum_val = 0
                rank = remain
                flag = 0
                result = [] 
        elif p_value < rank:
            if flag == 0:
                first = tmp
                flag = 1
            rank = rank - p_value
            sum_val += tmp
            result.append(tmp)
        else:
            tmp -= 1
else:
    print("Error")
