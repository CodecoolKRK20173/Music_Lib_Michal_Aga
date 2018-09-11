def import_albums(filename = "text_albums_data.txt"):
    with open(filename, "r") as data_import:
        import_list = []
        for line in data_import:
            import_list.append(line)
        import_list = [x.strip() for x in import_list]
        import_list = [line.split(',') for line in import_list]
        
        print(import_list)
        return import_list
"""
def export_albums(album_data, filename = "text_albums_data_export.txt"):
    with open(filename, "w") as data_export:
        for line in album_data:
            ','.join(line)
        print(album_data)
        """
        

import_albums()
#abc = [['Pink Floyd', 'The Dark Side Of The Moon', '1973', 'progressive rock', '43:00'], ['Britney Spears', 'Baby One More Time', '1999', 'pop', '42:20']]
export_albums(import_list)