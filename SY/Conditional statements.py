#ques 12
year=int(input("Enter the year to be checked:"))
if year%4==0:
    print("It is leap year")
else:
    print("It is not the leap year")
    
#ques 13
marks=int(input("Enter your marks:"))
if marks>=91:
    print("your grade is O")
elif marks>=81:
    print("Your grade is A+")
elif marks>=71:
    print("Your grade is A")
elif marks>=61:
    print("Your grade is B+")
elif marks>=51:
    print("Your grade is B")
elif marks>=41:
    print("Your grade is C")   
elif marks>=31:
    print("Your grade is D")
elif marks>=21:
    print("Your grade is E")
else:
    print("You are FAIL")
          
#ques 15
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if a>b:
    if a>c:
        print("A is the greatest number")
elif b>a:
    if b>c:
        print("B is the greatest number:")
else:
    print("C is the greatest number")
