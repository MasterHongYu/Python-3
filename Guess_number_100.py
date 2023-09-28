def Guess_number_100 ():

    import random
    # 確認位數的函數
    def digi():
        while True :
            try :
                digit = int(input("你想猜的數字範圍要是幾位數?(最少2位數，最多10位數)："))
                if 2 <= digit <= 10 :
                    return digit
            except :
                None
            Error()
    # 執行大小比較運算的函數
    def contract(min,max,ans,player_ans,digi_contract) :
        if 1 <= player_ans <= pow(10,digi_contract) - 1 :
            cheak = 0
            if player_ans == ans :
                cheak = 2
            if player_ans < min or player_ans > max :
                Error()
                cheak = 1
            if player_ans > min and player_ans < ans:
                min = player_ans
            if player_ans < max and player_ans > ans :
                max = player_ans
        else :
            Error()
            cheak = 1
        return min,max,cheak
    # 錯誤指示的函數
    def Error():
        print(f"輸入格式錯誤，或是輸入位數不正確，請再輸入一次，謝謝。\n")
    # 運行遊戲流程的函數
    def main():
        print("100 game")
        d,times = digi(),0
        print(f"\n遊戲規則：\n一、輸入的數字格式為連續的數字[例：10、123]\n二、請輸入題目範圍內的數字。\n三、若無遵照規則指示操作，則會跳出錯誤警示，不過程式碼不會崩潰，請放心。\n四、猜測總次數為{4 * d - 2}次。\n五、如果你想放棄本回合，請輸入\"F\"。\n")
        ans,min,max= random.randint(1,pow(10,d) - 1),1,pow(10,d) - 1
        while times < 4 * d - 2 :
            n = (input(f"請輸入{min}~{max}範圍內的數字，你還有{4 * d - 2 - times}次機會："))
            try :
                n = int(n)
                min,max,cheak = contract(min = min, max = max, ans = ans, player_ans = n, digi_contract = d)
                if cheak == 1 :
                    continue
                times += 1
                if cheak == 2 :
                    print(f"你贏了，總共花了{times}次")
                    rank(times=times,d=d)
                    break
                if times < 4 * d - 2 :
                    print(f"{min} < 答案 < {max}\n")
            except :
                if n == "F" :
                    print("您已放棄本回合的遊戲。")
                    break
                Error()
        else :
            print(f"你輸了，答案是{ans}")
        if input("要再玩一次嗎？如果要的話請輸入\"again\"，不用的話，請輸入除了\"again\"以外的值：\n") == "again" : 
            return "again"
        print("Bye:>")
    # 給予玩家等級的函數
    def rank(times,d) :
        if times <= 1.1 * d  :
            print("Rank：S\n")
        elif times <= 1.5 * d  :
            print("Rank：A\n")
        elif times <= 2.0 * d  :
            print("Rank：B\n")
        elif (times <= 2.5 * d and d <= 6) or (times <= 3 * d and d >= 7) :
            print("Rank：C\n")
        else :
            print("Rank：D\n")
            
    while main() == "again" :
        print()

if __name__ == "__main__" :
    Guess_number_100 ()
    