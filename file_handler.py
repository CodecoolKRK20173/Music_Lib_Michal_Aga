def import_albums(filename = "text_albums_data.txt"):
    with open(filename, "r") as data_import:
        import_list = []
        for line in data_import:
            import_list.append(line)
        import_list = [x.strip() for x in import_list]
        import_list = [line.split(',') for line in import_list]
        
        print(import_list)
        return import_list

def export_albums(album_data, filename = "text_albums_data_export.txt"):
    with open(filename, "w") as data_export:
        for line in album_data:
            ','.join(line)
        print(album_data)
        

"""
def export_inventory(inventory, filename="export_inventory.csv"):
    with open(filename, "w") as items_to_export:
        for key, value in inventory.items():
            for i in range(value):
                items_to_export.write(key + ',')
    with open(filename, 'rb+') as last_comma_deleter:
        last_comma_deleter.seek(-1, os.SEEK_END)
        last_comma_deleter.truncate()
        """



import_albums()
export_albums(import_list)