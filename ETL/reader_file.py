from ETL import config_parser
from ETL import load_properties
import os
import json


class Reader(config_parser.Parser):
    def parse(self, folder):
        file_paths = [folder + path for path in os.listdir(folder)]
        data = []

        for file_path in file_paths:
            with open(file_path, 'r') as file:
                data.append(json.load(file))

        return data


# load property, search after value that called folder.songs in the property
# folder = load_properties.Loader.load_properties('properties.properties', 'folder.songs')

# read the folder that contains all the json files and load them
# r = Reader()
# print(r.parse(folder))
