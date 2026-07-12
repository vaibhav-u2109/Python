"""try:
    num=int(input("enter a number"))
except:
    print("invalid input")"""
"""try:
    a=int(input("enter 1st number"))
    b=int(input("enter 2nd number"))
    result=a/b
    
except ZeroDivisionError:
    print("can't devide by zero")
except ValueError:
    print("invalid input")
else:
    print("result=",result)
finally:
    print("program ended")"""
print("1.add")
print("2.substract")
print("3.multiply")
print("4.devide")
choice=int(input("enter your choice"))
if choice==1:
    try:
        a=int(input("enter first number"))
        b=int(input("enter second number"))
        result=a+b
    except ValueError:
        print("invalid input")
    else:
        print("result=",result)
elif choice==2:
    try:
        a=int(input("enter first number"))
        b=int(input("enter second number"))
        result=a-b
    except ValueError:
        print("invalid input")
    else:
        print("result=",result)
elif choice==3:
    try:
        a=int(input("enter first number"))
        b=int(input("enter second number"))
        result=a*b
    except ValueError:
        print("invalid input")
    else:
        print("result=",result)
elif choice==4:
     try:
        a=int(input("enter first number"))
        b=int(input("enter second number"))
        result=a/b
     except ValueError:
        print("invalid input")
     
     except ZeroDivisionError:
         print("can't devide by zero")
     else:
        print("result=",result)
     finally:
         print("program ended")
else:
    print("invalid choice")


        