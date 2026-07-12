# i=1
# num=int(input("enter the number"))
# while i<=10 :
#     print(num*i)
#     i+=1
# tup=(1,4,9,16,25,36,49,64,81,100)
# idx=0
# x=36
# while idx < len(tup):
#     if tup[idx] == x:
#        print(tup[idx])
num=int(input("enter the multiple of 5:"))
while num%5!=0:
    print("try again")
    num=int(input("enter the multiple of 5"))
print("you entered a multiple of 5")
#     idx+=1
 # for loop

# list=[1,2,3,4,5]
# for i in list:
#     print(i)

#range function
# for i in range(5): 
#         print(i) #OUTPUT: 0,1,2,3,4
# for i in range(1,6):#(START,STOP)
#         print(i) #OUTPUT: 1,2,3,4,5
# for i in range(1,10,2): #(START,STOP,STEP)
#         print(i) #OUTPUT: 1,3,5,7,9

# #table of number
# num=int(input("enter the number :"))
# for i in range(1,11):
#     print(num*i)
# #sum of n natural numbers
# n=int(input("enter the number :"))
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i+=1
# print("sum of n natural numbers is :",sum)

# sum of n natural numbers using for loop
# n=int(input("enter the number :"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print("sum of n natural numbers is :",sum)

#factorial of a number using for loop
# num=int(input("enter the number :"))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print("factorial of a number is :",fact)