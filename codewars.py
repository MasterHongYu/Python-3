def sum_edges(n): 
    Sum,a = 0,5
    for i in range(sum(range(1,n + 1)) + 1) : 
        Sum += i
    for i in range(1,n+1) :
        if i >= 3 and i < n :
            Sum -= sum(range(a,a+(i-2)))
            a += i
    return(Sum)
print(sum_edges(int(input())))