#casting python

# name=input("Enter the name : ")

# english=int(input("Enter the mark english : "))
# math=int(input("Enter the mark math : "))
# sci=int(input("Enter the mark sci : "))

# total=english+math+sci

# percentage=(total/300)*100

# # print(f"student name {name} & percentage is {percentage}%")

# d={}

# d["name"]=input("Enter the name : ")
# d["age"]=int(input("Enter the age : "))
# d["height"]=int(input("Enter the height : "))
# d["student_stutes"]=input("Enter the student stutes : ")

# print(d)

# n=5

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# n=5
# for i in range(n):
#     for j in range(n):
#         print("$",end=" ")
#     print()

# n=5

# for i in range(n):
#     for j in range(i+1):
#         print('',end=' ')
#     for j in range(i,n):
#         print("*",end="")
#     print()

# n=5

# for i in range (1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     pritn(b)

# value = None

# if value:
#     print("value is true")
    
# else:
#     print("value is False")

#leap year program 

# year=(int(input("Enter a year (E.g yyyy) : ")))

# if (year%4==0 and year%100 !=0) and (year%100==0):
#     print(f"{year} is leap year")
# else:
#     print(f"{year} is not leap year")
# user_name="gaurav"
# password="Gaurav!21"

# username=input("Enter the user_name : ")
# password_user=input("Enter the password : ")


# if user_name==username:
#     if password_user==password:
#         print("sucessefully login")
#     else:
#         print("password is incorrect")
# else:
#     print("username is incurrect")

# mathematics=int(input("Enter the marks mathematics : "))
# physics=int(input("Enter the marks physics : "))
# chemistry=int(input("Enter the mark chemistry : "))

# if mathematics>=65 and physics>=55 and chemistry>=50:
#     print("student is eligibal to the admission")
# elif (mathematics+physics+chemistry>=180) or (mathematics+physics>140):
#     print("student is eligibal to seconde criteria")
# else:
#     print("student is not eligibal")

#function 

# def add(a,b):
#     print(a+b)

# add1=add(5,6)
# print(add1)

# def celsius_to_fahrenheit(celsius):
#     fahrenheit=(celsius * 9/5)+32
#     return fahrenheit
# temp_f=celsius_to_fahrenheit(25)
# print(temp_f)

# def add(num1,num2):
#     return num1+num2

# def sub(num1,num2):
#     return num1-num2

# def mult(num1,num2):
#     return num1*num2

# def div(num1,num2):
#     return num1/num2

# def avg(num1,num2):
#     return (num1+num2)/2

# print("calculater option : \n"
#       "1.addition\n"
#       "2.substraction\n"
#       "3.multipication\n"
#       "4.division\n"
#       "5.average\n")

# select=int(input("please select the option 1,2,3,4,5 : "))

# number1=int(input("Enter a first number : "))
# number2=int(input("Enter a second number : "))

# if select==1:
#     print(number1,"+",number2,"=",add(number1,number2))
# elif select==2:
#     print(number1,"-",number2,"=",sub(number1,number2))
# elif select==3:
#     print(number1,"*",number2,"=",mult(number1,number2))
# elif select==4:
#     print(number1,"/",number2,"=",div(number1,number2))
# elif select==5:
#     print("(",number1,"+",number2,")","/","2","=",avg(number1,number2))

# else:
#     print("Invalid Operetion pls try agian !")



# def add_numbers(*args):
#      return sum(args)
# op=add_numbers(1,2,3,4,5)
# print(op)

# def names(*name1):
#     for name in name1:
#         print("hello",name)
# op=names("santosh","raj","tushar","mayur")
# print(op)
# def data(**stud):
#     print(type(stud))
#     for keys,values in stud.items():
#         print(f'{keys}:{ values}')
# op =data(name="vaibhav",age=23, course="b.tech",college="zcoer")
# print(op)

def add(*numbers):
    total=0
    for number in numbers:
        total+=number
    return total
op=add(1,2,3,4,5)

op1=add(10,50)

print(op)
print(op1)