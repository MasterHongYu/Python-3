def Guess_number_1A2B ():

    import random
    # 確認位數的函數
    def digi():
        while True :
            try : 
                digital = int(input("你想猜幾位數字？\n(最少2位數，最多8位數)\n(5位數以上的不推薦，除非你想挑戰自我)："))
                if 2 <= digital <= 8 : 
                    return digital
            except : 
                Error()
            Error()
    # 生成答案的函數
    def answer(n):
        return random.sample(range(10),n)
    # 確認玩家輸入的答案格式，是否正確的函數
    def guess(times_guess,digi_guess) :
        input_guess = input(f"請輸入{digi_guess}位數字，你還有{(2 * digi_guess) + 4 - times_guess}次機會：")
        try :
            guess = [int(i) for i in input_guess.split()]
            if len(guess) == digi_guess and len(set(guess)) == digi_guess and (0 <= i < 10 for i in guess) :
                return guess
            elif len(guess) == 1 and len(list(input_guess)) == digi_guess and len(set(list(input_guess))) == digi_guess:
                guess = [int(i) for i in list(input_guess)]
                return guess
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
        print("%d A %d B\n"%(An,Bn))
        if An == digi_AnBn :
            print(f"你贏了!總共花了{times_AnBn}次。\n") 
            return "win"
    # 錯誤函數
    def Error ():
        print(f"輸入格式錯誤，或是輸入位數不正確，請再輸入一次，謝謝。\n")
        return "?"
    # 確認玩家是否要再玩一輪的函數
    def play_again():
        if input("要再玩一次嗎？如果要的話請輸入\"again\"，不用的話，請輸入除了\"again\"以外的值：\n") == "again" :
            return "again"
    # 運行遊戲流程的函數
    def main():
        print("1A2B Game")
        d = digi() 
        print(f"\n遊戲規則：\n一、輸入的數字格式為2種：(一)連續的數字(二)以空格隔開的數字。\n[例：(一) 1234 (二) 1 2 3 4 ]\n二、不可輸入重複數字。\n三、答案的數字範圍在0~9，並且不會有重複數字。\n四、若無遵照規則指示操作，則會跳出錯誤警示，不過程式碼不會崩潰，請放心。\n五、猜測總次數為{2 * d + 4}次。\n")
        ans,times = answer(d),0
        #print(ans)
        while times < (2 * d + 4):
            player_guess = guess(times,d)
            if player_guess == "?" : 
                continue
            times += 1
            if (res := AnBn(player_guess,ans,d,times))  == "win" :
                rank(times,d)
                break
        else : 
            print(f"遊戲結束，你輸了，正確號碼為{''.join([str(i) for i in ans])}，太可惜了。\n")

        if (again := play_again()) == "again" : 
            main()
        else :
            print("Bye:>")
    # 給予玩家的等第
    def rank(times,d) :
        if times == 1 :
            print("Rank：God")
        elif times <= 1.1 * d  :
            print("Rank：S")
        elif times <= 1.5 * d  :
            print("Rank：A")
        elif times <= 2.0 * d  :
            print("Rank：B")
        elif (times <= 2.3 * d and d >= 4) or (times <= 2.5 * d and d < 4)  :
            print("Rank：C")
        else :
            print("Rank：F")
   
    main()

Guess_number_1A2B()

    

