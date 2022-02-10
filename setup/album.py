from setup import song


class Album:
    def __init__(self, id: str, name: str, songs={}):
        self.id = id
        self.name = name
        self.songs = songs

    def add_song(self, new_song: song.Song):
        self.songs[new_song.id] = new_song
