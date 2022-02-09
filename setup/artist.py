from setup import album


class Artist:
    def __init__(self, id: str, name: str, albums=[]):
        self.id = id
        self.name = name
        self.albums = albums

    def add_album(self, new_album: album.Album):
        self.albums.append(new_album)

