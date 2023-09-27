'''
def add(*arg) :
    total = 0
    for i in arg :
        total += i
    return total
def sub(*arg) :
    total = 0
    for i in arg :
        total -= i
    return total
'''
print(' '.join([str(i) for i in [int(i) for i in range(1,119)]]))

def Squential_Search(data,n):
    times = 0
    for i in data:
        times += 1
        if n == i:
            return f"該資料位於data陣列中的第{data.index(i)}項，總共比對{times}次。"
    return "找不到該筆資料。"
print(Squential_Search(data := [(i) for i in input("請輸入一串陣列：").split()],n := (input("請輸入欲尋找的資料："))))

#當我在data值輸入[3,5,7,9,11,15]，n值輸入11之後，最後結果會印出 The index of this value in the Data array is at 2。
#該程式碼為我們小組自行編寫，未拷貝網上的程式碼。'''

def Binary_Search(data,n):
    dataoSorted = sorted(data)
    left,right,times = 0,len(dataoSorted) - 1,0
    while left <= right:
        times += 1
        if n < dataoSorted[(m := (left + right) // 2)] :
            right = m - 1
        elif n > dataoSorted[m] :
            left = m + 1
        elif n == dataoSorted[m]:
            return f"該資料位於data陣列中的第{data.index(dataoSorted[m])}項，總共比對{times}次。"
    return "找不到該筆資料。"
            
Binary_Search(data := [int(i) for i in input("請輸入一串數字陣列(data)：").split()],n := int(input("請輸入欲尋找的數字：")))

'''
widght,height,n = [float(i) for i in input().split()]
matrix,anwser= [[float(i)for i in input().split()]for j in range(4)],[]
for i in range(height/2):
    for j in range(widght/2):
        a = 0
        for i2 in range(n):
            for j2 in range(n):
                a += matrix[i+i2][j+j2]
        print(a/4,end=' ')
        '''










