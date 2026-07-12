def palindrome(s):
    reveresed=s[::-1]
    if s==reveresed:
        print("palidrome")
    else:
        print("not palidrome")
userinput=input("enter your string")
palindrome(userinput)
