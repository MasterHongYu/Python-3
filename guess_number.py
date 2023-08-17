def guess_number_game ():

    # 確認位數的函數
    def digi():
        while True :
            try : 
                digital = int(input("你想猜幾位數字？(最少3位數，最多7位數)："))
            except : 
                Error()
                continue
            if 3 <= digital <= 7 : 
                break
            Error()
        return digital
    # 生成答案的函數
    def answer(n):
        from random import choice as c
        number,ans = [int(i) for i in range(10)],[]
        for i in range(n) :
            ans.append(c(number))
            number.remove(ans[i])
        return(ans)
    # 確認玩家輸入的答案格式，是否正確的函數
    def guess(times_guess,digi_guess) :
        try :
            guess = [int(i) for i in input(f"請輸入{digi_guess}位數字，並且每個數字間都要有空格，不可輸入重複數字，你還有{(2 * digi_guess) + 2 - times_guess}次機會：").split()]
            if len(guess) == digi_guess and len(set(guess)) == digi_guess and (0 <= i < 10 for i in guess) :
                return(guess)
            else : 
                errorkey = Error()
                return errorkey
        except :
            errorkey = Error()
            return errorkey
    # 執行1A2B的運算
    def AnBn(playerGuess,ans,digi_AnBn,times_AnBn):
        An,Bn = 0,0
        for i in range(digi_AnBn):
            if playerGuess[i] == ans[i] : 
                An += 1
            elif playerGuess[i] in ans : 
                Bn += 1 
        print("%d A %d B"%(An,Bn))
        if An == digi_AnBn :
            print(f"你贏了!總共花了{times_AnBn}次。") 
            return "win"
    # 錯誤函數
    def Error ():
        print(f"輸入格式錯誤，或是輸入位數不正確，請再輸入一次，謝謝。")
        return "?"
    # 確認玩家是否要再玩一輪的函數
    def play_again():
        if input("要再玩一次嗎？如果要的話請輸入\"again\"，不用的話，請輸入除了\"again\"以外的值：") == "again" :
            return "again"
    # 運行遊戲流程的函數
    def main():
        print("1A2B Game")
        d = digi() 
        ans,times = answer(d),0
        #print(ans)
        while times < (2 * d + 2):
            check = guess(times,d)
            if check == "?" : 
                continue
            times += 1
            if (res := AnBn(check,ans,d,times))  == "win" :
                break
        else : 
            print(f"遊戲結束，你輸了，正確號碼為{''.join([str(i) for i in ans])}，太可惜了。")

        if (again := play_again()) == "again" : 
            main()
        else :
            print("Bye:>")
   
    main()

guess_number_game()
    

