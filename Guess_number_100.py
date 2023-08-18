def Guess_number_100 ():
    
    def anwser() :
        import random as ran 
        ans = ran.randint(1,99)
        print(ans)
        return ans
    
    def contract(player_ans,min,max,ans) :
        if 1 <= player_ans <= 99 :
            if player_ans == ans :
                print('Youwin!')
                return -1,-1
            if player_ans > min and player_ans < ans:
                min = player_ans
            if player_ans < max and player_ans > ans :
                max = player_ans
        else :
            Error()
            return -2,-2

    def Error():
        print("輸入錯誤")
        
    def main():
        ans,min,max = anwser(),1,99 
        while True :
            try :
                n = int(input("請輸入1~99範圍內的數字"))
                min,max = contract(n,min,max,ans)
                if min == max == -2 :
                    continue
                if min == max == -1 :
                    print(f"Youwin,{ans}")
                    break
                print(f"{min} < 答案 < {max}")
            except :
                Error()
    main()
Guess_number_100 ()
    