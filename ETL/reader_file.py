from ETL import config_parser
import os
import json


class Reader(config_parser.Parser):
    def parse(self, parse_value):
        file_paths = [parse_value + path for path in os.listdir(parse_value)]
        data = []

        for file_path in file_paths:
            with open(file_path, 'r') as file:
                data.append(json.load(file))

        return data


