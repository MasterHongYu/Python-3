def Guess_number_100 ():
    
    def anwser() :
        import random as ran 
        ans = ran.randint(1,99)
        #print(ans)
        return ans
    
    def contract(player_ans,min,max,ans) :
        if 1 <= player_ans <= 99 :
            if player_ans == ans :
                cheak = 2
            if player_ans < min or player_ans > max :
                Error()
                cheak = 1
            if player_ans > min and player_ans < ans:
                min,cheak = player_ans,0
            if player_ans < max and player_ans > ans :
                max,cheak = player_ans,0
            return min,max,cheak
        else :
            Error()
            cheak = 1
            return min,max,cheak

    def Error():
        print("輸入格式錯誤")
        
    def main():
        ans,min,max,times= anwser(),1,99,0
        while times < 8 :
            cheak = 0
            try :
                n = int(input(f"請輸入{min}~{max}範圍內的數字，你還有{8-times}次機會："))
                min,max,cheak = contract(n,min,max,ans)
                if cheak == 1 :
                    continue
                if cheak == 2 :
                    times += 1
                    print(f"你贏了，總共花了{times}次")
                    break
                print(f"{min} ≤ 答案 ≤ {max}")
                times += 1
            except :
                Error()
        else :
            print(f"你輸了，答案是{ans}")
    main()
Guess_number_100 ()
    