def menu():
    print("************MENU MUSIC**************\n")

    choice = input("""
                      A: Import/Export
                      B: Display Albums
                      C: Album Search
                      D: Reports
                      Q: Quit

                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        import_albums() #function from file_handler.py
    elif choice == "B" or choice =="b":
        viewstudentdetails()
    elif choice == "C" or choice =="c":
        search_menu()
    elif choice=="D" or choice=="d":
        producereports()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You must only select either A,B,C, or D.")
        print("Please try again")
        menu()

def search_menu():
    search_choice = input("""
                      1: Find albums by genre
                      2: Find albums by year range
                      3: Show the shortest album
                      4: Show the longest album
                      5: Find albums created by given artist
                      6: Find album by album name
                      7: Quit to main menu

                      Please enter your choice: """)    

    if search_choice == '1':
        genre_search()
    elif search_choice == '2':
        year_range()
    elif search_choice == '3':
        show_shortest_longest_album(shortest)
    elif search_choice == '4':
        show_shortest_longest_album(longest)
    elif search_choice == '5':
        artist_search()
    elif search_choice == '6':
        album_name_search()
    elif search_choice == '7':
        menu()
    else:
        print("Please enter a number from 1 to 7.")
        search_menu()

