def Guess_number_1A2B ():

    import random;import time
    # 確認位數的函數
    def digi():
        while True :
            try : 
                digital = int(input("你想猜幾位數字？(最少2位數，最多10位數，建議2-5位數)："))
                if 2 <= digital <= 10 : 
                    return digital
            except : None
            Error()
    # 判斷玩家所輸入的答案格式，是否為正確的函數
    def guess(times_guess,digi_guess) :
        while True :
            input_guess = input(f"請輸入{digi_guess}位數字，你還有{(2 * digi_guess) + 4 - times_guess}次機會：")
            try :
                guess = [int(i) for i in list(input_guess) if i != " "]
                if len(guess) == len(set(guess)) == digi_guess and all(0 <= i < 10 for i in guess) :
                    return guess
            except :
                if input_guess == "F" :
                    print("您已放棄本回合的遊戲。")
                    return input_guess
            Error()
    # 執行1A2B運算的函數
    def AnBn(playerGuess,ans,digi_AnBn,times_AnBn):
        An,Bn = 0,0
        for i in range(digi_AnBn):
            if playerGuess[i] == ans[i] : 
                An += 1
            elif playerGuess[i] in ans : 
                Bn += 1 
        if An == digi_AnBn :
            print(f"你贏了!總共花了{times_AnBn}次。") 
            Time ();rank(times = times_AnBn, d = digi_AnBn);Time ()
            return "win"
        print(f"第{times_AnBn}次猜測：{An} A {Bn} B\n")
    # 錯誤指示的函數
    def Error ():
        print(f"輸入格式錯誤，或是輸入位數不正確，請再輸入一次，謝謝。\n")
        Time ()
    # 運行遊戲流程的函數
    def main():
        print("1A2B Game")
        d,times,list = digi(),0,[]
        print(f"\n遊戲規則：\n一、輸入的數字格式：只能包含阿拉伯數字與空格，且阿拉伯數字的數量要與所猜之位數相等。\n二、不可輸入重複數字。\n三、答案的數字範圍在0~9，並且不會有重複數字。\n四、若無遵照規則指示操作，則會跳出錯誤警示，不過程式碼不會崩潰，請放心。\n五、猜測總次數為{2 * d + 4}次。\n六、如果你想放棄本回合，請輸入\"F\"。\n")
        Time ();ans = random.sample(range(10),d)
        #print(ans)
        while times < (2 * d + 4):
            player_guess = guess(times_guess = times, digi_guess = d)
            if player_guess in list :
                print("這個數字你猜過了，稍微冷靜一下。\n")
                Time ()
                continue
            list.append(player_guess)
            times += 1
            if player_guess == "F" or AnBn(playerGuess = player_guess, ans = ans, digi_AnBn = d, times_AnBn = times) == "win" :
                if player_guess == "F" :
                    Time ();print(f"正確號碼為{''.join([str(i) for i in ans])}。");Time ()
                break
        else : 
            print(f"遊戲結束，你輸了，正確號碼為{''.join([str(i) for i in ans])}，太可惜了。\n")
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
        elif (times <= 2.5 * d and d <= 6) or (times <= 2.3 * d and d >= 7) :
            print("Rank：C\n")
        else :
            print("Rank：D\n")
    
    def Time () :
        time.sleep(0.25)
    
    while main() == "again" :
        print()

if __name__ == '__main__' :
    Guess_number_1A2B()

    

