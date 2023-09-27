import os;import time
game1 = r"/Users/chengyuchang/Desktop/程式-Program/VS code/Python 3/Guess_number_1A2B.py"
game2 = r"/Users/chengyuchang/Desktop/程式-Program/VS code/Python 3/Guess_number_100.py"
while True:
    if __name__ == "__main__" :
        if (choice := int(input("歡迎遊玩小遊戲！以下是遊戲編號：\n    1.1A2B\n    2.終極數字\n請輸入你想玩的遊戲的數字編號："))) == 1:
            if os.path.exists(game1):
                import Guess_number_1A2B
                print("成功離開遊戲");time.sleep(1)
            else : "存取錯誤";continue
        elif choice == 2:
            if os.path.exists(game2):
                import Guess_number_100
                print("成功離開遊戲");time.sleep(1)
            else: "存取錯誤";continue
        elif choice == 0:
            print("Bye!");break
        else :
            print('輸入格式錯誤，請再輸入一次');continue

