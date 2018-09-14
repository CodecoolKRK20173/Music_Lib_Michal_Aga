import inputs
import display
import os

def display_raport(album_list):
    os.system("clear")
    print("""'\033[1;32m
  _____            _____   ____  _____ _______ 
 |  __ \     /\   |  __ \ / __ \|  __ \__   __|
 | |__) |   /  \  | |__) | |  | | |__) | | |   
 |  _  /   / /\ \ |  ___/| |  | |  _  /  | |   
 | | \ \  / ____ \| |    | |__| | | \ \  | |   
 |_|  \_\/_/    \_\_|     \____/|_|  \_\ |_|   
                                               
  \033[1;m                                             
""")
    print("Number of artists: {}".format(count_artists(album_list)))
    print("Number of albums:  {}".format(count_albums(album_list)))
    print("Number of genres:  {}".format(count_genres(album_list)))
    print("\nThe longest album: ")
    inputs.show_shortest_longest_album(album_list, 'longest')
    print("\nThe shortest album: ")
    inputs.show_shortest_longest_album(album_list, 'shortest')
    #print("\n\tThe oldest album: ")
    #print("\n\tThe newest album: ")
    
    print("\nAll imported albums: ")
    display.display_table_header()
    for album in album_list:
        display.display_album_to_print(album)

def count_artists(input_list):
    artists_number = len(input_list)+1
    artist_to_compare = input_list[0][0]
    for line in input_list:
        if artist_to_compare == line[0]:
            artists_number -= 1
    return artists_number

def count_albums(input_list):
    album_number = len(input_list)+1
    album_to_compare = input_list[0][1]
    for line in input_list:
        if album_to_compare == line[1]:
            album_number -= 1
    return album_number

def count_genres(input_list):
    genres_number = len(input_list)+1
    genres_to_compare = input_list[0][3]
    for line in input_list:
        if genres_to_compare == line[3]:
            genres_number -= 1
    return genres_number


#album_list = [['Pink Floyd', 'The Dark Side Of The Moon', '1973', 'progressive rock', '43:00'], ['Britney Spears', 'Baby One More Time', '1999', 'pop', '42:20'], ['The Beatles', 'Revolver', '1966', 'rock', '34:43'], ['Deep Purple', 'Machine Head', '1972', 'hard rock', '37:25'], ['Old Timers', 'Old Time', '966', 'ancient', '123:45'], ['Pink Floyd', 'Wish You Were Here', '1975', 'progressive rock', '44:28'], ['Boston', 'Boston', '1976', 'hard rock', '37:41'], ['Monika Brodka', 'Granada', '2010', 'pop', '37:42'], ['David Bowie', 'Low', '1977', 'rock', '38:26'], ['rock', 'rock', '966', 'pop', '13:37'], ['Massive Attack', 'Blue Lines', '1991', 'hip hop', '45:02']]
#print(count_genres(album_list))
#display_raport(album_list)