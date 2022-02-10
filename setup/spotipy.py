from setup import artist


class Spotipy:
    def __init__(self):
        self.artists = {}

    def add_artist(self, new_artist: artist.Artist):
        self.artists[new_artist.id] = new_artist
