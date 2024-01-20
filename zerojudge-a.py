#a002
#a = [int(i) for i in input().split()]
#print(a[0]+a[1])

#a003
# Bd = [int(i) for i in input().split()]
# S = (Bd[0] * 2 + Bd[1]) % 3
# if S == 0 :
#     print("普通")
# elif  S == 1:
#     print("吉")
# else :
#     print("大吉")

#a004
# def indentify(x):
#     if (x % 4) == 0:
#         if (x % 100) != 0 or (x % 400) == 0 :
#             return("閏年")
#     return("平年")
# while True:
#     try :
#         print(indentify(int(input())))
#     except :
#         break

#a005
# def S():
#     sp = [int(i) for i in input().split()]
#     if (sp[1] / sp[0]) == (sp[2] / sp[1]) :
#         sp.append(int(sp[3]*(sp[1] / sp[0])))
#     else :
#         sp.append(int(sp[3]+(sp[1] - sp[0])))
#     print(" ".join([str(i) for i in sp]))
# for j in range(int(input())):
#     S()

#a006
# S = [int(i) for i in input().split()]
# if  (S[1] ** 2)-(4 * S[0] * S[2]) < 0 :
#     print("No real root")
# else :
#     X1 = int((-S[1]+(((S[1] ** 2)-(4 * S[0] * S[2]))**(1/2)))/(2*S[0]))
#     X2 = int((-S[1]-(((S[1] ** 2)-(4 * S[0] * S[2]))**(1/2)))/(2*S[0]))
#     if X1 != X2 :
#         print(f"Two different roots x1={X1} , x2={X2}")
#     else :
#         print(f"Two same roots x={X1}")

#009
# word = []
# for i in input():
#     I = ord(i)
#     if I < 39 :
#        I += 87 
#     I -= 7
#     word.append(chr(I))
# print("".join(word))

#a010
# a,ans = int(input()),[]
# b = a
# c = a
# if c > 10000000  :
#      c = c / 10 * 2
# for i in range(2,round(c/2)+2):
#     if a % i != 0 : continue
#     power = 0
#     while a % i == 0:
#         power += 1
#         a /= i
#     if power > 1:
#         ans.append(f"{i}^{power}")  
#     elif power == 1:
#         ans.append(f"{i}")
# if len(ans) == 0:
#     print(b)
# else:
#     print(" * ".join(ans))

#a013
# def transfromNumber(a):
#     RomeToNumber = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
#     b,res = [],0
#     for i in a:
#         b.append(RomeToNumber[i])
#     b.append(0)
    
#     for i in range(0,len(b) -1) :
#         if b[i] < b[i+1]:
#             res += (b[i+1] - b[i])
            
#         elif b[i] >= b[i+1] :
#             if i == 0 :
#                 res += (b[i])
#             elif b[i] <= b[i-1]:
#                 res += (b[i])
#     return(res)

# def transfromRome(c):
#     res = []
#     if c == 0 :
#         res.append("ZERO")

#     if c >= 1000 :
#         res.append("M"*(c//1000))
#         c -= 1000 * (c//1000)
#     if c >= 900 :
#         res.append("C")
#         res.append("M")
#         c -= 900
#     if c >= 500 :
#         res.append("D")
#         res.append("C"*((c-500)//100))
#         c -= (500 + 100 * ((c-500)//100))
#     if c >= 400 :
#         res.append("C")
#         res.append("D")
#         c -= 400

#     if c >= 100 :
#         res.append("C"*(c//100))
#         c -= 100 * (c//100)
#     if c >= 90 :
#         res.append("X")
#         res.append("C")
#         c -= 90
#     if c >= 50 :
#         res.append("L")
#         res.append("X"*((c-50)//10))
#         c -= (50 + 10 * ((c-50)//10))
#     if c >= 40 :
#         res.append("X")
#         res.append("L")
#         c -= 40
    
#     if c >= 10 :
#         res.append("X"*(c//10))
#         c -= 10 * (c//10)
#     if c >= 9 :
#         res.append("I")
#         res.append("X")
#         c -= c
#     if c >= 5 :
#         res.append("V")
#         res.append("I"*(c-5))
#         c -= c
#     if c == 4 :
#         res.append("I")
#         res.append("V")
#         c -= c
#     if c > 0 :
#         res.append("I"*c)
    
#     return(res)

# while True :
#     s = [str(i) for i in input().split()]
#     if "#" in s :
#         break 
#     print("".join( transfromRome( abs( transfromNumber(s[0]) - transfromNumber(s[1]) ) ) ) )

