def guess_number_game ():

    def answer(n):
        from random import choice as c
        number,ans = [int(i) for i in range(10)],[]
        for i in range(n) :
            ans.append(c(number))
            number.remove(ans[i])
        return(ans)
    
    def guess(k,d) :
        try :
            guess = [int(i) for i in input(f"請輸入{d}位數字，並且每個數字間都要有空格，不可輸入重複數字，你還有{10 - k}次機會：").split()]
            if len(guess) == d and len(set(guess)) == d and (0 <= i < 10 for i in guess) :
                return(guess)
            else : 
                errorkey = Error()
                return errorkey
        except :
            errorkey = Error()
            return errorkey

    def Error ():
        print(f"輸入格式錯誤，或是輸入位數不正確，請再輸入一次。")
        return "?"
    
    def AnBn(playerGuess,ans,l):
        An,Bn = 0,0
        for i in range(l):
            if playerGuess[i] == ans[i] : 
                An += 1
            elif playerGuess[i] in ans : 
                Bn += 1 
        print("%d A %d B"%(An,Bn))
        if An == l : 
            return "win"
        
    def play_again():
        if input("要再玩一次嗎？如果要的話請輸入\"again\"，不用的話，請輸入除了\"again\"以外的值：") == "again" :
            return "again"
    
    def digi():
        while True :
            try : 
                digital = int(input("你想猜幾位數字？(最少3位數，最多7位數)："))
            except : 
                None
            if 3 <= digital <= 7 : 
                break
            Error()
            continue
        return digital

    def main():
        print("1A2B Game")
        n = digi() 
        ans,times = answer(n),0
        #print(ans)
        while times < 10:
            check = guess(times,n)
            if check == "?" : 
                continue
            times += 1
            if (res := AnBn(check,ans,n))  == "win" :
                print(f"你贏了!總共花了{times}次。")
                break
        else : 
            print(f"遊戲結束，你輸了，正確號碼為{ans[0]}{ans[1]}{ans[2]}{ans[3]}，太可惜了。")

        if (again := play_again()) == "again" : 
            main()

    main()
    print("bye")
guess_number_game()
    

