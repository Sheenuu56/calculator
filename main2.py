def Add():
   num1=int(input("enter the number 1"))
   num2=int(input("enter the number 2"))
   sum=num1+num2
   print(f"the sum of the two numbers is {sum}")

def Subtract():
    num1=int(input("enter the number 1"))
    num2=int(input("enter the number 2"))
    dif= num1-num2
    print(f"the difference of the two numbers is {dif}")

def Multiply():
    num1=int(input("enter the number 1"))
    num2=int(input("enter the number 2"))
    pro= num1*num2
    print(f"the product of the two numbers is {pro}")

def Divide():
    num1=int(input("enter the number 1"))
    num2=int(input("enter the number 2"))
    div= num1/num2
    print(f"amswer is {div}")

if __name__ == "__main__":
    print("CALCULATOR")
    while True:
        print("\n")
        print("Please select one of the following options:")
        print("-------------------------------------------")
        print("1. Add ")
        print("2. Subtract")
        print("3. Mu;tiply")
        print("4. Divide")

        choice = input("Enter your choice number: ")
     
        if (choice == "1"):
          Add()
        elif (choice == "2"):
          Subtract()
        elif (choice == "3"):
          Multiply()
        elif (choice == "4"):
          Divide()
        else: 
          print("Invalid Choice")
    
    print("Goodbye!!")