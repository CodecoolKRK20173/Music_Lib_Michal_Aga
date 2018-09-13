"""
def print_album_info(album):
    artist_index = 0
    name_index = 1

    print('Album: {} by {}'.format(album[name_index], album[artist_index]))
    print(' | '.join(album[2:]))


def print_albums_list(albums_data):
    for album in albums_data:
        print(' | '.join())


def print_program_menu(menu_commands):
    for option in menu_commands:
        print(str(menu_commands.index(option)) + '----->' + option)


def print_command_result(message):
    vertical_spacing = 2
    print(vertical_spacing * '\n' + message)

def print_error_message(message):
    print("ERROR: " + str(message))
"""   
def display_album_to_print(album_to_print):
    print('+' + '=' * 30 + '+' + '=' * 30 + '+' + '=' * 10 + '+' + '=' * 30 + '+' + '=' * 10 + '+')
    print('|{:^30}'.format("ARTIST NAME") + ('|{:^30}'.format("ALBUM NAME"))+ ('|{:^10}'.format("YEAR")) + ('|{:^30}'.format("GENRE")) + ('|{:^10}|'.format("TIME")) )
    for my_album in album_to_print:
        print('+' + '=' * 30 + '+' + '=' * 30 + '+' + '=' * 10 + '+' + '=' * 30 + '+' + '=' * 10 + '+')
        print('|{:^30}|{:^30}|{:^10}|{:^30}|{:^10}|'.format(my_album[0], my_album[1], my_album[2], my_album[3], my_album[4]))

album_list= [['Pink Floyd', 'The Dark Side Of The Moon', '1973', 'progressive rock', '43:00'], ['Britney Spears', 'Baby One More Time', '1999', 'pop', '42:20'], ['The Beatles', 'Revolver', '1966', 'rock', '34:43'], ['Deep Purple', 'Machine Head', '1972', 'hard rock', '37:25'], ['Old Timers', 'Old Time', '966', 'ancient', '123:45'], ['Pink Floyd', 'Wish You Were Here', '1975', 'progressive rock', '44:28'], ['Boston', 'Boston', '1976', 'hard rock', '37:41'], ['Monika Brodka', 'Granada', '2010', 'pop', '37:42'], ['David Bowie', 'Low', '1977', 'rock', '38:26'], ['rock', 'rock', '966', 'pop', '13:37'], ['Massive Attack', 'Blue Lines', '1991', 'hip hop', '45:02']]
                            
display_album_to_print(album_list)