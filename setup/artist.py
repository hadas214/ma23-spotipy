from setup import album


class Artist:
    def __init__(self, id: str, name: str, albums={}):
        self.id = id
        self.name = name
        self.albums = albums

    def add_album(self, new_album: album.Album):
        self.albums[new_album.id] = new_album

    def check_album(self, id_album: str):
        if id_album in self.albums.keys():
            return True
        return False




