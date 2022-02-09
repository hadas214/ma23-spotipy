from setup import artist


class Spotipy:
    def __init__(self):
        self.artist = {}

    def add_artist(self, new_artist: artist.Artist):
        self.artist.append(new_artist)