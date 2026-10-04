while True:
    print("1 : sum")
    print("2 : substraction")
    print("3 : multiplication")
    print("4 : devision")
    print("5 : reminder")
    print("6 : square")
    print("7 : For exit this program")

    choice = int(input("enter your choice : "))

    if choice == 1:
        a = int(input("enter first number : "))
        b = int(input("enter second number : "))
        print("sum of two number is : ",a+b)

    elif choice == 2:
        a = int(input("enter first number : "))
        b = int(input("enter second number : "))
        print("substraction of two number is : ",a-b)

    elif choice == 3:
        a = int(input("enter first number : "))
        b = int(input("enter second number : "))
        print("multiplication of two number is : ",a*b)

    elif choice == 4:
        a = int(input("enter first number : "))
        b = int(input("enter second number : "))
        print("devision of two number is : ",a/b)

    elif choice == 5:
        a = int(input("enter first number : "))
        b = int(input("enter second number : "))
        print("remainder of two number is : ",a%b)

    elif choice == 6:
        a = int(input("enter first number : "))
        
        print(a**2)

    elif choice == 7:
        print("you are exit of this program")
        break

    
    
        

        

