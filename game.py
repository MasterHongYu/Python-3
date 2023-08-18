say = print
say("Hello")

import os
game1 = r"/Users/chengyuchang/Desktop/程式-Program/VS code/Python 3/Guess_number_1A2B.py"
if os.path.exists(game1):
    import Guess_number_1A2B 
else :
    print("檔案存取錯誤")

