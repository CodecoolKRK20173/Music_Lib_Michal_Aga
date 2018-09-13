import file_handling
import main # pytanie bo tutaj chyba będziemy mieć menu.py ? nie ?

def get_albums_by_genre(albums, genre):
    genre_on_list = []
    for i in range(len(albums)):
        genre_on_list.append(albums[i][3])

    if genre in genre_on_list:
        albums_by_genre = []
        for i in range(len(albums)):
            if albums[i][3] == genre:
                albums_by_genre.append(albums[i])
    else:
        raise ValueError("Wrong genre type")

    return albums_by_genre


def get_genre_stats(albums):
    genre_stats = {}
    for i in range(len(albums)):
        if albums[i][3] in genre_stats:
            genre_stats[albums[i][3]] += 1
        else:
            genre_stats[albums[i][3]] = 1
    return genre_stats

def get_last_oldest(albums):

    earliest = albums[0][2]
    last_oldest = albums[0]

    for i in range(len(albums)-1):
        if int(earliest) >= int(albums[i+1][2]):
            earliest = albums[i+1][2]
            last_oldest = albums[i+1]


    return last_oldest


def get_last_oldest_of_genre(albums, genre):
    """
    Get last album with earliest release year in given genre
    """
    albums_list_by_genre = get_albums_by_genre(albums, genre)
    last_oldest_of_genre = get_last_oldest(albums_list_by_genre)

    return last_oldest_of_genre


"""albums = file_handling.import_data(filename='albums_data.txt')
genre = main_program.get_input("Please enter genre: rock ")
print(get_last_oldest_of_genre(albums, genre))  ???? zobaczcie prosze czy errory wam wywala"""

def get_longest_album(albums):

#    Get album with biggest value in length field

    biggest_length = albums[0][4].replace(":", ".")
    longest_album = albums[0]

    for i in range(len(albums)-1):
        if float(biggest_length) < float(albums[i+1][4].replace(":", ".")):
            biggest_length = albums[i+1][4].replace(":", ".")
            longest_album = albums[i+1]

    return longest_album

def get_total_albums_length(albums):
    """
    Get sum of lengths of all albums in minutes, rounded to 2 decimal places
    """
    minutes = []
    secound = []
    time = []
    for i in range(len(albums)):
        time = albums[i][4].split(":")
        minutes.append(int(time[0]))
        secound.append(int(time[1]))

    albums_length = (sum(minutes)*60 + sum(secound))/60

    return round(albums_length, 2)
