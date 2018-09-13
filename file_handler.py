def import_albums(filename = "/home/michal/Codecool/Python/TW week #2/Music_Lib_Michal_Aga/text_albums_data.txt"):
    try:
        with open(filename, "r") as data_import:
            album_list = []
            for line in data_import:
                album_list.append(line)
            album_list = [x.strip() for x in album_list]
            album_list = [line.split(',') for line in album_list]
            
            print("Imported data from {}".format(filename))

            return album_list
    except:
        TypeError('Cannot find file!')
"""
def export_albums(album_data, filename = "text_albums_data_export.txt"):
    with open(filename, "w") as data_export:
        for line in album_data:
            ','.join(line)
        print(album_data)
        """
        

#import_albums()
#abc = [['Pink Floyd', 'The Dark Side Of The Moon', '1973', 'progressive rock', '43:00'], ['Britney Spears', 'Baby One More Time', '1999', 'pop', '42:20']]
#export_albums(import_list)