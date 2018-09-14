def import_albums(filename = "text_albums_data.txt"):
    try:
        with open(filename, "r") as data_import:
            album_list = []
            for line in data_import:
                album_list.append(line)
            album_list = [x.strip().split(',') for x in album_list]
           #album_list = [line.split(',') for line in album_list]
            
            print("\t\tImported data from {}".format(filename))

            return album_list
    except FileNotFoundError:
        print('Cannot find file!')

