def sum_edges(n): 
    Sum,a = sum(range(1,(sum(range(1,n + 1))+ 1))),5
    for i in range(3,n) :Sum -= sum(range(a,a+(i-2)));a += i
    return(Sum)
for i in list(map(sum_edges,[int(i) for i in input().split()])) :
    print(i)