# def palindrome(name):
#     # name="madam"
#     if name==name[::-1]:
#         print("name is palindrome")
#     else:
#         print("name is not palindrome")
# palindrome("mom")

# def palindrome():
#     name = input("Enter the name : ")
#     if name==name[::-1]:
#         print("name is palindrome")
#     else:
#         print("name is not palindrome")
# palindrome()
# def twonumber(num1,num2):
#     if num1>num2:
#         return num1+num2
#     else:
#         return num2-num1
# num1=int(input('enter num1 : '))
# num2=int(input("enter num2 : "))

# op=twonumber(num1,num2)
# print(op)

# def palindrome(name):
#     if name==name[::-1]:
#         return "name is palindrome"
#     else:
#         return "name is not palindrome"
# name=input("Enter the name : ")
# op=palindrome(name)
# print(op)

# def ver(*name):
#     return len(name)
# result=ver(1,2,3,4)
# print(result)

# def var(**name):
#     return len(name)
# result=var(name="gaurav",age=21,city="pune")
# print(result)

# def index(string):
    
#     for i in range(len(string)):
       
#         print(i,string[i])
        
# result=index("coding part is done")
# print(result)


# def squere(l):
#     result=[]
#     for i in l:
        
#         result.append(i**2)
#     return result
# l=[1,2,4,3]

# print(squere(l))


# def digit(ster):
#     result=[]
#     for i in ster:
#         if i.isdigit():
#             result.append(i)
#     print(result)
# digit("hello123")

# def number(num1,num2,num3):
#     result=(num1+num2)-num3
#     return result


# number1=int(input("Enter the number1 : "))
# number2=int(input("Enter the number2 : "))
# number3=int(input("Enter the number3 : "))
 
# op=number(number1,number2,number3)
# print(op)

# def squ(num1):
#     return num1**2

# def cube(num1):
#     return num1**3

# def squroot(num1):
#     return num1**(1/2)

# def cuberoot(num1):
#     return num1**(1/3)

# print("given option :-\n"
#       "1.square\n"
#       "2.cube\n"
#       "3.square root\n"
#       "4.cube root")
# select=int(input("Enter the option 1,2,3,4 : "))
# number=int(input("Enter the number : "))
# if select==1:
#     print(number,"**2","=",squ(number))
# elif select==2:
#     print(number,"**3","=",cube(number))
# elif select==3:
#     print(number,"**(1/2)","=",squroot(number))
# elif select==4:
#     print(number,"**(1/3)","=",cuberoot(number))
    
# else:
#     print("optin is Ivalid")

# def caleculate(n):
    
#     square=n**2
#     cube=n**3
#     square_root=n**(1/2)
#     cube_root=n**(1/3) 
    
#     print("square",square)   
#     print("cube",cube)
#     print("square_root",square_root)
#     print("cube_root",cube_root)
# number=int(input("enter the number : "))

# print(caleculate(number))

# def char(string):
#     # char=[]
#     # digit=[]
#     # special=[]
#     for i in string:
#         if i.isalpha():
#             # char.append(i)
#             print("charecture :",i)
            
#         elif i.isdigit():
#             # digit.append(i)
#             print("digit : ",i)
#         else:
#             # special.append(i)
#            print("special : ",i)
#         print("special : ",i)       
# st=input("Enter string : ")
# print(char(st))

# def char(ch):
#     if ('a'<=ch<='z') or ('A'<=ch<='z'):
#         print("character : ",ch)
#     elif '0'<=ch<='9':
#         print("digit : ",ch)
#     else:
#         print("special : ",ch)
# op=input("Enter the char : ")
# char(op)
# def ite(iterable):
    
#     if isinstance(iterable,(list,set,tuple,dict)):
        
#         print(iterable[::-1])
# op=[1,2,3,4]
# ite(op)

# def func(s,a):
#     while a < len(s):
#         print(s[a],end="")
#         a+=2
# func("TRACXN",1)

# def argu(s,i):
#     # a=s.split()
#     while i <len(s):
#         if i>=5:
#             print(s)
#         i+=1
#     print(s)
# argu("sauhuidn nhdiusain as ",1)


# def dic(s):
#     d={}
#     for i in s:
#         if i.isalpha():
#             d[i]=ord(i)
#     print(d)
# dic("khgfgh")

# def rev(data):
#     if isinstance(data,(str,tuple,list)):
#         print(data[::-1])
#     else:
#         print(type(data))
        
# rev([1,2,3,4,5,6])
# rev((1,2,3,4,5,))
# rev({1,3,4,5})
# def char(cha):
#     dig=[]
#     for ch in cha:
#         if ch.isalpha():
#             print("char is alphabate:",ch)
#         elif ch.isdigit():
#             dig.append(ch)
#             print(dig)
#             # print("char is digit:",ch)LJ
#         else:
#             print("special char :",ch)
# # print(dig)
# name=input("Enter the char : ")
# char(name)


# def iter(data):
#     count=0
#     for i in data:
#         count+=1
#     return count
#     # print(count)
# # a="python"
# print(iter("uhiudbb"))

# def argument(**name):
#    return len(name)
# result=argument(name="gaurav",age=12,city="pune")
# print(result)

# def cal(num):
#     count=0
#     for i in num:
#         count=i+count
#     return count
# data=[1,2,3,4,5]
# print(cal(data))

# def large(num1,num2,num3):
#     if num1>num2 and num1>num3:
#         return num1       
#     elif num2>num1 and num2>num3:
#         return num2
#     else:
#         return num3
# op=large(675,25,1)
# print(op)
 
 
# def vowels(string):
#     i=0
#     while i <len(string):
#         if string.lower()=='aoeiu':
#             i+=1
#     print( i)
        
# data=vowels("hello")
# print(data)
# def string(name):
#   i=0
#   while i<len(name):
#     if name[i].lower() in "aeiou":
#       print(name[i])
#       i+=1
# n=string("hello")
# print(n)


# s = 'Hello guys Good morning python is a programming language'

# i=0

# while i<=len(s):
#   if s.isspace():
#     print(i)
#     i+=1

# num=int(input("enter the number : "))

# for i in range(1,11):
#   print(num*i)

# l=["vaidegi","ashwini","patil","srinidhi","susmitha","rahul","priyanka","usha"]

# i=0
# while i<=len(l):
#   if len(l[i])%2==0:
#     print(l[i])
#   i+=1


# def stirng(name):
#   i=0
#   while i<len(name):
#     if name[i].lower() in 'aeoiu':
#       print(name[i])
#     i+=1
    
# data=stirng("hello")

# print(data)


# x=10
# def data ():
#   print(x)
#   #x=12
# data()


# name="hello"

# print(list(enumerate(name)))

# s="python"

# for i in range(0,len(s)):
#   print([[i,s[i]]],end=" ")

# s=[1,2,3,4,44,55,4,3,2,1]

# print(set(s))
# s="hello word"
# d={}
# for i in s:
#   d[i]=ord(i)
# print(d)
  
# l=["yellow","yellow","red","black","pink","orange","green","red","pink","yellow"]
# d={}


# for i in l:
  
#   d[i]=l.count(i)
# print(d)


for i in range(6):
  for j in range(1,i+1):
    print("*",end=" ")
  print()
for i in range(6):
  for j in range(i-1,5):
    print("*",end=" ")
  print()
