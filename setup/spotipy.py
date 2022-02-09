from setup import artist


class Spotipy:
    def __init__(self):
        self.artist = {}

    def add_artist(self, new_artist: artist.Artist):
        self.artist[new_artist.id] = new_artist.name
