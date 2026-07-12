# #function defination
"""def cal_sum(a, b): #function defination with parameters

    sum = a + b
    print("the sum of two numbers is :", sum)
    
    cal_sum(10, 20)#function call with arguments
    cal_sum(5, 15)"""
"""def cal_largest(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c
result=cal_largest(10,20,300)
print(result)"""
"""def sum(*num):
    s=0
    for i in num:
        s+=i
    return s
result=sum(10,20,30,40,40,60)
print(result)
"""
"""def student(name,marks,city):
    print(name)
    print(marks)
    print(city)
    
student(marks=90,name="vaibav",city="varanasi")"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
while True:
    try:
        print("1.add")
        print("2.substract")
        print("3.multiply")
        print("4.devide")
        print("5.exit")
        choice=int(input("enter your choice"))
        if choice==5:
          print("thanks for using calculator")
          break
        if choice in[1,2,3,4,]:
         a=int(input("enter first number"))
         b=int(input("enter second number"))
        if choice==1:
          result=add(a,b)
        elif choice==2:
          result=subtract(a,b)
        elif choice==3:
          result=multiply(a,b)
        elif choice==4:
          result=divide(a,b)
        elif choice==5:
           print("thanks for using calculator")
           break
        else:
           print("invalid choice")
           continue
    except ValueError:
     print("invalid input")
    except ZeroDivisionError:
     print("can not devide by zero")
    else:
       print(result)
    
 

 