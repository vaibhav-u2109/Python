# class Student:#creating a class named student
#     name="vaibhav"
#     age=19

# s1=Student() #creating an object of the class student
# print(s1.name)
# print(s1.age)

# class Student:
#     def __init__(self,name,age): #constructor
#         self.name=name
#         self.age=age

# s1=Student("vaibhav",19)
# print(s1.name)
# print(s1.age)

# class Student:
#     def __init__(self,name,age): #constructor
#         self.name=name
#         self.age=age

#     def welcome(self):#method
#         print("welcome:",self.name)
#     def your_age(self):
#             print("your age is:",self.age)
        
# s1=Student("vaibhav",19)
# s1.welcome()#calling the method welcome
# s1.your_age()#calling the method your_age


# class Student:
#     def __init__(self,name,marks): #constructor
#         self.name=name
#         self.marks=marks

#     def average(self):
#             sum=0
#             for val in self.marks:
#              sum+=val
#             print("hello",self.name,"average marks is:",sum/len(self.marks))

# s1=Student("vaibhav",[90,85,88])
# s1.average()

#Abstraction=>hiding the implementation details and showing only the functionality to the user
# class Car:
#     def __init__(self):
#         self.accelerate=False
#         self.brake=False
#     def start(self):
#         # self.accelerate=True
#         # self.brake=True
#         print("car started")

# c1=Car()
# c1.start()

#question=>create a class account with attributes account number and balance.
#  create methods to credit and debit amount from the account and display the current balance.

# class Account:
#     def __init__(self,account_number,balance):
#         self.account_number=account_number
#         self.balance=balance  
    
#     def credit(self,amount):
#         self.balance+=amount
#         print("Amount credited:",amount)
#         print("Current balance:",self.balance)
#     def debit(self,amount):
#         self.balance-=amount
#         print("Amount debited:",amount)
#         print("Current balance:",self.balance)

# a1=Account("1234567890",1000)
# print("balance:",a1.balance)
# a1.credit(500)
# a1.debit(200)

# class car:
#     def __init__(self,brand,):
#         self.brand=brand
#     @staticmethod
#     def start():
#        print("car started")
#     @staticmethod
#     def stop():
#         print("car stopped")

# class toyatacar(car):#inheritance => child class toyatacar inherits the properties of parent class car
#         def __init__(self,name):
#          self.name=name
# class fotuner(toyatacar):#multilevel inheritance => child class fotuner inherits the properties of parent class toyatacar which in turn inherits the properties of parent class car
#     def __init__(self,type):
#         self.type=type

# c1=toyatacar("innova")
# print(c1.name)
# c2=fotuner("petrol")
# print(c2.type)  
# print(c1.start())

class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
            print("area of circle is:",3.14*self.radius*self.radius)
    def parimeter(self):
            print("perimeter of circle is:",2*3.14*self.radius)

c1=circle(5)
c1.area()
c1.parimeter()
        
  


