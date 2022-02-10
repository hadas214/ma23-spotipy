from setup import song


class Playlist:
    def __init__(self, name, songs=[]):
        self.name = name
        self.songs = songs

    def add_song(self, new_song: song.Song):
        self.songs.append(new_song)
