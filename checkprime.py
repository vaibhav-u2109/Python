# num=int(input("Enter a number: "))
# for i in range(2,num):
#     if num%i==0:
#         print(num,"is not prime")
#         break
# else:
#     print(num,"is prime")

"""print all prime numbers between 2 and 100"""


for num in range(2,100):
   for i in range(2,num):
       if num%i==0:
             break
   else:
      print(num,"is prime")
        
        
    
