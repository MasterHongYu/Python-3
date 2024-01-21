# a001. 哈囉
# print("hello, "+input())

# a002. 簡易加法
# a = [int(i) for i in input().split()]
# print(a[0]+a[1])

# a003. 兩光法師占卜術
# Bd = [int(i) for i in input().split()]
# S = (Bd[0] * 2 + Bd[1]) % 3
# if S == 0 :
#     print("普通")
# elif  S == 1:
#     print("吉")
# else :
#     print("大吉")

# a004. 文文的求婚
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

# a005. Eva 的回家作業
# def S():
#     sp = [int(i) for i in input().split()]
#     if (sp[1] / sp[0]) == (sp[2] / sp[1]) :
#         sp.append(int(sp[3]*(sp[1] / sp[0])))
#     else :
#         sp.append(int(sp[3]+(sp[1] - sp[0])))
#     print(" ".join([str(i) for i in sp]))
# for j in range(int(input())):
#     S()

# a006. 一元二次方程式
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

# a009. 解碼器 
# word = []
# for i in input():
#     I = ord(i)
#     if I < 39 :
#        I += 87 
#     I -= 7
#     word.append(chr(I))
# print("".join(word))

# a010. 因數分解
# a,ans = int(input()),[]
# b = a
# c = a
# if c > 10000000  :
#      c = c // 10 * 2
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

# a013. 羅馬數字
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

# a015. 矩陣的翻轉
# def transfromMatrix():
#     r = [int(i) for i in input().split()]
#     matrix = [[int(i) for i in input().split()] for j in range(r[0])]
#     for i in range(r[1]) :
#         matrixT = []
#         for j in range(r[0]) :
#             matrixT.append(matrix[j][i])
#         print(" ".join([str(k) for k in matrixT]))
# while True :
#     try :
#         transfromMatrix()
#     except:
#         break

# a017. 五則運算
#一、
# def newfma():
#     import math
#     def indentifyOperate(tp):
#         res,key = int(tp[0]),0

#         for i in range(2):
#             tp.append("0")

#         for i in range(1,len(tp)-2,2) :

#             if tp[i+2] not in ("*","%","/") and key == 0:
#                 if tp[i] == "+" :
#                     res += int(tp[i+1])
#                 elif tp[i] == "-" :
#                     res -= int(tp[i+1])
#                 elif tp[i] == "*" :
#                     res *= int(tp[i+1])
#                 elif tp[i] == "%" :
#                     res %= int(tp[i+1])
#                 elif tp[i] == "/" :
#                     res = math.floor(res / (int(tp[i+1])))
#                 continue

#             elif key == 1 :
#                 if tp[i] == "*" :
#                     total *= int(tp[i+1])
#                 elif tp[i] == "%" :
#                     total %= int(tp[i+1])
#                 elif tp[i] == "/" :
#                     total = math.floor(total / int(tp[i+1]))
#                 if tp[i+2] not in ("*","%","/") :
#                     key = 0
#                 if key == 0:
#                     if operate == "+" :
#                         res += total
#                     elif operate == "-" :
#                         res -= total
#                     total = 0
#                 continue

#             elif (tp[i] in ("*","%","/")) and key == 0:
#                 if tp[i] == "*" :
#                     res *= int(tp[i+1])
#                 elif tp[i] == "%" :
#                     res %= int(tp[i+1])
#                 elif tp[i] == "/" :
#                     res = math.floor(res / int(tp[i+1]))
#                 continue

#             else :
#                 operate,key,total = tp[i],1,int(tp[i+1])
#         return res


#     formula = [str(i) for i in input().split()]
#     while "(" in formula :
#         for i in range(len(formula)) :
#             if formula[i] == "(":
#                 indexStart = i
#             if formula[i] == ")" :
#                 indexEnd = i
#                 break
#         temporary = []
#         for i in range(indexStart + 1,indexEnd) :
#             temporary.append(formula[i])
#         for i in range(indexEnd - indexStart+1) :
#             formula.pop(indexStart)
#         formula.insert(indexStart,indentifyOperate(temporary) )
#     print(indentifyOperate(formula))   

# while True :
#     try :
#         newfma()
#     except:
#         break
#二、
# while True :
#     try :
#         print(eval(input().replace("/",'//')))
#     except :
#         break


# a020. 身分證檢驗
# def indentity():
#     number,n = input(),[]
#     for i in number :
#         n.append(i)
#     rigion = {"A":(1,0),'B':(1,1),'C':(1,2),'D':(1,3),'E':(1,4),'F':(1,5),'G':(1,6),'H':(1,7),'I':(3,4),'J':(1,8),'K':(1,9),'L':(2,0),"M":(2,1),"N":(2,2),"O":(3,5),'P':(2,3),"Q":(2,4),"R":(2,5),"S":(2,6),"T":(2,7),"U":(2,8),"V":(2,9),"W":(3,2),"X":(2,0),"Y":(3,1),"Z":(3,3)}
#     b = rigion[(n[0])][0] + rigion[(n[0])][1] * 9
#     for i in range(1,9):
#         b += (int(n[i]) * (9-i))
#     if ( b + int(n[-1])) % 10 == 0 :
#         print("real")
#     else :
#         print("fake")
# indentity()       

# a021. 大數運算
# print(eval(input().replace('/','//')))

# a022. 迴文
# s,a = input(),[]
# for i in s:
#     a.append(i)
# for i in range((len(a)//2)):
#     if a[i] !=  a[-i-1]:
#         print("no")
#         s = " "
#         break
# if s != " ":
#     print('yes')
