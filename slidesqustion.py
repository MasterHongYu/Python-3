class Search:

    def __init__(self) :
        self.data = [int(i) for i in input("請輸入一串數字陣列(data)：").split()]
        self.n = int(input("請輸入欲尋找的數字："))

    def Squential_Search(self):
        times = 0
        for i in self.data:
            times += 1
            if self.n == i:
                return f"該資料位於data陣列中的第{self.data.index(i)}項，使用循序搜尋法，總共比對{times}次。"
        return "找不到該筆資料。"

    def Binary_Search(self):
        dataoSorted = sorted(self.data)
        left,right,times = 0,len(dataoSorted) - 1,0
        while left <= right:
            times += 1
            if self.n < dataoSorted[(m := (left + right) // 2)] : 
                right = m - 1
            elif self.n > dataoSorted[m] : 
                left = m + 1
            elif self.n == dataoSorted[m]:
                return f"該資料位於data陣列中的第{(self.data).index(dataoSorted[m])}項，使用二分搜尋法，總共比對{times}次。"
        return "找不到該筆資料。"

a = Search()
print(a.Squential_Search())
print(a.Binary_Search())




#---------------

電話號碼 = { 
    "臺北" : 2 , 
    "桃園" : 3 , 
    "新北" : 2 , 
    "新竹" : 3 , 
    "苗栗" : 37 , 
    "臺中" : 4 , 
    "宜蘭" : 3 , 
    "高雄" : 7
      }
def a(data,n):
    for key in data.keys():
        if key == n :
            print(f"{n}的電話號碼為0{data[key]}。")
            return None
    print("找不到該筆資料。")
a(電話號碼,"臺中")

#---------------

print(' '.join([str(i) for i in [int(i) for i in range(1,119)]]))

