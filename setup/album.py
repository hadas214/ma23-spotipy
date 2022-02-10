from setup import song


class Album:
    def __init__(self, id: str, name: str, songs={}):
        self.id = id
        self.name = name
        self.songs = songs

    def add_song(self, new_song: song.Song):
        current_song = song.Song(new_song.name, new_song.id, new_song.popularity)
        self.songs[current_song] = current_song
