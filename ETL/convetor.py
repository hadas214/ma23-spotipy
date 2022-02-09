from ETL import config_parser
from setup import song, album, artist


class Reader(config_parser.Parser):
    def parse(self, folder: str):
        file_paths = [folder + path for path in os.listdir(folder)]
        data = []

        for file_path in file_paths:
            with open(file_path, 'r') as file:
                data.append(json.load(file))

        return data