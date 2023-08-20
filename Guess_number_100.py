def Guess_number_100 ():

    def digi():
        while True :
            try :
                digit = int(input("你想猜的數字範圍要是幾位數?(最少2位數，最多6位數)："))
                if 2 <= digit <= 6 :
                    return digit
                Error()
            except :
                Error()

    def anwser(d) :
        import random as ran 
        ans = ran.randint(1,pow(10,d) - 1)
        #print(ans)
        return ans
    
    def contract(player_ans,min,max,ans,digi_contract) :
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
            return min,max,cheak
        else :
            Error()
            cheak = 1
            return min,max,cheak

    def Error():
        print(f"輸入格式錯誤，或是輸入位數不正確，請再輸入一次，謝謝。\n")
    
    def play_again():
        if input("要再玩一次嗎？如果要的話請輸入\"again\"，不用的話，請輸入除了\"again\"以外的值：\n") == "again" :
            return "again"
        
    def main():
        print("100 game")
        d = digi()
        ans,min,max,times= anwser(d),1,pow(10,d) - 1,0
        while times < 4 * d - 2 :
            try :
                n = int(input(f"請輸入{min}~{max}範圍內的數字，你還有{4 * d - 2 - times}次機會："))
                min,max,cheak = contract(n,min,max,ans,d)
                if cheak == 1 :
                    continue
                if cheak == 2 :
                    times += 1
                    print(f"你贏了，總共花了{times}次")
                    break
                if times < 4 * d - 2 :
                    print(f"{min} < 答案 < {max}\n")
                times += 1
            except :
                Error()
        else :
            print(f"你輸了，答案是{ans}")

        if (again := play_again()) == "again" : 
            main()
        else :
            print("Bye:>")

    main()
Guess_number_100 ()
    