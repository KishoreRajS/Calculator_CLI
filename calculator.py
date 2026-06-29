#function
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    if b==0:
        return "error! Division by zero is not allowed."
    return a/b
#main program 
while True:
    print ("1. Addition")
    print ("2. subtraction")
    print ("3. multiplication")
    print ("4. division")
    print ("5. Exit")
    
    choice= input("enter your choice:")
    if choice=="5":
        print (" thank you for using the calculator")
        break 
    if choice in ("1","2","3","4"):
        num1= float(input("enter first number:"))
        num2= float(input("enter the second number:"))
        if choice == "1":
            print ("result=", add(num1,num2))
        elif choice=="2":
            print ("result=",subtract(num1,num2))
        elif choice =="3":
            print ("result=",multiplication(num1,num2))
        elif choice =="4":
            print ("result=",division(num1,num2))
else:
    print("invaild choice! please enter a number betweeen 1 and 5.")            