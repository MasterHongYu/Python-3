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
# 法一、
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
# 法二、
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
#     rigion = {"A":(1,0),'B':(1,1),'C':(1,2),'D':(1,3),'E':(1,4),'F':(1,5),'G':(1,6),'H':(1,7),'I':(3,4),'J':(1,8),'K':(1,9),'L':(2,0),"M":(2,1),"N":(2,2),"O":(3,5),'P':(2,3),"Q":(2,4),"R":(2,5),"S":(2,6),"T":(2,7),"U":(2,8),"V":(2,9),"W":(3,2),"X":(3,0),"Y":(3,1),"Z":(3,3)}
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

# a024. 最大公因數(GCD)
# def greatestCommonFactor (a,b):
#     if a % b != 0 :
#         k = greatestCommonFactor(b,a % b)
#     else :
#         k = b
#     return (k)

# a = [int(i) for i in input().split()]
# if a[1] > a[0] :
#     a[0] , a[1] = a[1] , a[0]
# print(greatestCommonFactor(a[0],a[1]))

# 034. 二進位制轉換
# 法一
# def binary():
#     n,a,k = int(input()),[0],1
#     if n != 0 :
#         for i in range(1,n+1):
#             if i % (2 ** k) == 0:
#                 k += 1
#                 for j in range(len(a)) : 
#                     a[j] = 0
#                 a.append(0)
#                 a[0] = 1
#             else :
#                 a[-1] += 1
#             while 2 in a :
#                 b = a.index(2)
#                 a[b-1] += 1
#                 a[b] -= 2
#     print("".join([str(i) for i in a]))
# while True:
#     try :
#         binary()
#     except:
#         break
# 法二
# while True:
#     try :
#          print(bin(int(input()))[2:])
#     except:
#         break

# a038. 數字翻轉
# def revolve():
#     n,a,b,k = input(),[],0,0
#     for i in n:
#         a.insert(0,i)
#     if '0' in a :
#         for i in range(len(a)) :
#             if int(a[i]) != 0 :
#                 k += 1
#                 break
#             b += 1
#         for i in range(b) :
#             if a.count("0") == 1 and k == 0:
#                 break
#             a.pop(0)
            
#     print(''.join([str(i) for i in a]))
# revolve()

# a040. 阿姆斯壯數
# def  Armstrongnumber(a):
#     b,c = [],0
#     for i in str(a) :
#         b.append(int(i))
#     for i in range(len(b)):
#         c += b[i] ** len(b)
#     if c == a :
#         return (str(a))
#     return "-1"

# s = [int(i) for i in input().split()]
# res = []
# for i in range(s[0],s[1]+1):
#     p = Armstrongnumber(i)
#     if int(p) >= 0  :
#         res.append(p)
# if len(res) == 0 :
#     print('none')
# else:
#     print(" ".join(res))

# a042. 平面圓形切割
# while True :
#     try :
#         n = int(input())
#         print(n**2-n+2)
#     except :
#         break

# a044. 空間切割
# 法一(遞迴，但有限制)
# def a(n,k):
#     k += int((n**2-n+2)/2)
#     if n > 0 :
#         k += a(n-1,0)
#     return k 
# while True:
#     try:
#         print(a(int(input()),0))
#     except:
#         break
# 法二
# while True :
#     try :
#         n = int(input())
#         print(int((n**3+5*n+6)/6))
#     except :
#         break

# a053. Sagit's 計分程式

# n = int(input())

# if n > 40 :
#     print(100)
# elif 21 <= n and n <= 40 :
#     print(60+n)
# elif 11 <= n and n <= 20 :
#     print(40+2*n)
# else :
#     print(6*n)

# a054. 電話客服中心
# rigion = {"A":(1,0),'B':(1,1),'C':(1,2),'D':(1,3),'E':(1,4),'F':(1,5),'G':(1,6),'H':(1,7),'I':(3,4),'J':(1,8),'K':(1,9),'L':(2,0),"M":(2,1),"N":(2,2),"O":(3,5),'P':(2,3),"Q":(2,4),"R":(2,5),"S":(2,6),"T":(2,7),"U":(2,8),"V":(2,9),"W":(3,2),"X":(3,0),"Y":(3,1),"Z":(3,3)}
# indentify,res = input(),0
# for i in range(len(indentify)):
#     res += int(indentify[i]) * (8-i)
# k = (10 - int(indentify)%10) + 10 - res % 10
# if k >= 10 :
#     k %= 10
# ans = []
# for key,value in rigion.items() :
#     if (value[0] + value[1] * 9) % 10 == k :
#         ans.append(key)
# print("".join(ans))

# a058. MOD3
# n,k,kp,kpp = int(input()),0,0,0
# for i in range(n):
#     a = int(input())
#     if a % 3 == 0 :
#         k += 1
#     if a % 3 == 1 :
#         kp += 1
#     if a % 3 == 2 : 
#         kpp += 1
# print(f'{k} {kp} {kpp}')

# a059. 完全平方和
# n,t = int(input()),0
# for i in range(n):
#     t += 1
#     a,b,res =int(input()),int(input()),0
#     for j in range(b-a):
#         k = ( (j+a) ** (1/2) )
#         if k == round(k):
#             res += int(j+a)
#     print(f"Case {t}: {res}")

# a065. 提款卡密碼
# a,s,ans = input(),[],[]
# for i in a:
#     s.append(ord(i))
# for i in range(len(s)-1) :
#     ans.append(str(abs(s[i+1]-s[i])))
# print("".join(ans))

# a104. 排序
# def a(n):
#     s,res = [int(i) for i in input().split()],[]
#     for i in range(n):
#         res.append(str(min(s)))
#         s.remove(min(s))
#     print(" ".join(res))

# while True :
#     try :
#         a(int(input()))
#     except :
#         break

# a121. 質數又來囉


def is_prime(k):
    if k < 2 or (k % 2 == 0 and k != 2) or (k % 3 == 0 and k != 3) or (k % 5 == 0 and k != 5) :
        return False
    for j in range(2,round(k**(1/2))+1) :
        if k % j == 0 :
            return False
    return True

def main(n,m):
    s = (m-n)+1
    for i in range(n,m+1):
        if is_prime(i) == False :
            s -= 1
    return s


while True:
    try :
        x,y = map(int,input().split())
        print(main(x,y))
    except EOFError:
        break

import time
start_time = time.time()
print(main(3,7))
print(main(6,6))
print(main(30,50))
end_time = time.time()
print(end_time,start_time)