from ETL import config_parser
from ETL import load_properties
import os
import json


class Reader(config_parser.Parser):
    def parse(self, folder):
        file_paths = [folder + path for path in os.listdir(folder)]

        for file_path in file_paths:
            with open(file_path, 'r') as file:
                data = json.load(file)
            print(data)


# load property, search after value that called folder.songs in the property
# folder = load_properties.Loader.load_properties('properties.properties', 'folder.songs'

# read the folder that contains all the json files and load them
# r = Reader()
# r.parse(folder)
