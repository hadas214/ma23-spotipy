from abc import ABC, abstractmethod
from ETL import load_properties
from ETL import transform
from ETL import reader_file
from playlist_feature import playlist, user


class Search:
    def __init__(self):
        # load property, search after value that called folder.songs in the property
        folder = load_properties.Loader.load_properties(r'C:\ma23\Spotipy\properties.properties', 'folder.songs')

        # read the folder that contains all the json files and load them
        reader = reader_file.Reader()
        data = reader.parse(folder)

        self.transformer = transform.Transform()
        self.transformer.parse(data)

    @abstractmethod
    def search(self, search_by):
        pass
