my_dict = {}
while True:
    print("1 . Add Contacts ")
    print("2 . View Contacts ")
    print("3 . Search Contacts ")
    print("4 . Exit ")

    choice = int(input("enter your choice : "))

    if choice == 1:
        a = input("enter a name : ")
        b = int(input("enter number : "))
        my_dict[a]=b
        print("contact added succesfully")
        print(my_dict)
        

    elif choice ==2:
        print("all contacts ",my_dict)

    elif choice ==3:
        c = input("enter name : ").lower()
        found = False
        for name , number in my_dict.items():
            if name.lower() == c:
                print(f"number found : {number}")
                found = True
                break
        if not found:
                print("contacts not found")

    elif choice == 4:
        print("you are exit....")
        print("thank you")
        break




         



         
