def menu():
    print("************MENU MUSIC**************")
    #time.sleep(1)
    print()

    choice = input("""
                      A: Export/Imports
                      B: Displays Albums
                      C: Search / Handling user
                      D: Reports
                      Q: Quit/Log Out

                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        enterstudentdetails()
    elif choice == "B" or choice =="b":
        viewstudentdetails()
    elif choice == "C" or choice =="c":
        searchbyid()
    elif choice=="D" or choice=="d":
        producereports()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You must only select either A,B,C, or D.")
        print("Please try again")
        menu()
