import sys

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
        genre_search(album_list)
    elif search_choice == '2':
        year_range()
    elif search_choice == '3':
        show_shortest_longest_album(album_list, shortest)
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


def genre_search(input_albums):
    ask_user_about_genre = input("Please enter genre you want to find : ")
    for album in input_albums:
        if album[3] == ask_user_about_genre:
            print('| {} | {} | {} | {} | {} |'.format(album[0], album[1], album[2], album[3], album[4]))
        
     
   
def year_search(input_albums):
    loop_handling = True
    while loop_handling:
        year_range = input('Enter a year range from which you want to find albums (yyyy-yyyy): ')
        if '-' in year_range:
            year_range = year_range.split('-')
            year_range = [int(year) for year in year_range]
            print(year_range)
            for album in input_albums:
                if int(album[2]) in range(year_range[0],year_range[1]+1):
                    print('| {} | {} | {} | {} | {} |'.format(album[0], album[1], album[2], album[3], album[4]))
                else:
                    print('No album from given year range.')
                    break
            loop_handling = False
        else:
            print('Please write year range in yyyy-yyyy format.')
           
            
def show_shortest_longest_album(input_albums):
    actual_longest_time = 0
    longest_album = []
    for album in input_albums:
        album_time = album[4].split(':')
        album_time = [int(time) for time in album_time]
        album_time = album_time[0]*60 + album_time[1]
        print(album_time)
       
        if album_time > actual_longest_time:
            actual_longest_time = album_time
            longest_album = album
    print(longest_album)


album_list = [['Pink Floyd', 'The Dark Side Of The Moon', '1973', 'progressive rock', '43:00'], ['Britney Spears', 'Baby One More Time', '1999', 'pop', '42:20'], ['The Beatles', 'Revolver', '1966', 'rock', '34:43'], ['Deep Purple', 'Machine Head', '1972', 'hard rock', '37:25'], ['Old Timers', 'Old Time', '966', 'ancient', '123:45'], ['Pink Floyd', 'Wish You Were Here', '1975', 'progressive rock', '44:28'], ['Boston', 'Boston', '1976', 'hard rock', '37:41'], ['Monika Brodka', 'Granada', '2010', 'pop', '37:42'], ['David Bowie', 'Low', '1977', 'rock', '38:26'], ['rock', 'rock', '966', 'pop', '13:37'], ['Massive Attack', 'Blue Lines', '1991', 'hip hop', '45:02']]
#year_search(album_list)
show_shortest_longest_album(album_list)