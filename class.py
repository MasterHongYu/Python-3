#class phone:
#    lens = 3
#    def __init__(self,make,model,color):
#        self.make = make
#        self.model = model
#        self.color = color
#    def open(self) :
#        print(self.model,"已開機")
#phone1 = phone(make="Apple",model="iPhone",color="Yellow")
#phone1.lens = 2
#phone2 = phone(make="Samsung",model="Galaxy",color="Purple")
#print(phone1.make,phone1.model,phone1.lens)
#print(phone2.make,phone2.model,phone2.lens)
#phone1.open()
#-------------------------------------------
"""class animal:
    alive = True
   def eat(self) :
        print("The rabbit is eating")
        return self
    def sleep(self) :
        print("The rabbit is sleeping")
        return self
class rabbit(animal):
    def jump(self) :
        print("The rabbit is jump")
        return self
writeRabbit = rabbit()
writeRabbit.eat().sleep().jump()  """
#---------------------------------------------
"""class Rectangle() :
    def __init__(self,length,width) :
            self.length = length
            self.width = width
class Square(Rectangle) :
    def __init__(self,length,width) :
        super().__init__(length,width)
class Cube(Rectangle) :
    def __init__(self, length, width,height):
        super().__init__(length, width)
        self.height = height
    def cube(self) :
         print(self.height*self.length*self.width)
cube = Cube(3,3,3)
cube.cube()"""
#--------------------------------------------------
'''i = 0
while (a := int(input())) != 0 :
    i += a
print(i)'''
from random import choice

def generate_answer():
    number_pool = [i for i in range(10)]
    answer = []
    for _ in range(4):
        digit = choice(number_pool)
        answer.append(digit)
        number_pool.remove(digit)
    return answer

def get_guess():
    while True:
        try:
            guess = [int(i) for i in input("請輸入四位數字，並且每個數字間都要有空格：").split()]
            if len(guess) == 4 and len(set(guess)) == 4 and all(0 <= digit < 10 for digit in guess):
                return guess
            else:
                print("輸入格式錯誤，請重新輸入。")
        except ValueError:
            print("輸入格式錯誤，請重新輸入。")

def evaluate_guess(target, guess):
    A_count = sum(1 for i in range(4) if guess[i] == target[i])
    common_digits = set(target) & set(guess)
    B_count = len(common_digits) - A_count
    return A_count, B_count

def main():
    print("1A2B Game")
    play_again = True
    while play_again:
        answer = generate_answer()
        k = 0
        while k < 10:
            k += 1
            guess = get_guess()
            A_count, B_count = evaluate_guess(answer, guess)
            print(f"{A_count} A {B_count} B")
            if A_count == 4:
                print(f"你贏了！總共花了{k}次。")
                break
        else:
            print(f"遊戲結束，你輸了，正確號碼為{''.join(str(digit) for digit in answer)}，太可惜了。")
        
        play_again = input("要再玩一次嗎？如果要的話請輸入\"again\"，不用的話，請輸入除了\"again\"以外的值。") == "again"

    print("bye")

if __name__ == "__main__":
    main()



        

