#第一題
'''
n = int(input())
all = [int(i) for i in input().split()]
print(" ".join([str(i) for i in sorted(all)]))

def a(list):
    unpassExam,passExam = [],[]
    for i in list :
        if i < 60 :
            unpassExam.append(i)
        if i >= 60 :
            passExam.append(i)
    return unpassExam,passExam

case1,case2 = a(all)

try :
    print(max(case1))
except :
    print("best case")

try :
    print(min(case2))
except :
    print("worst case")
'''
#第二題

    
