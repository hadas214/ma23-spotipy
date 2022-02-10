from playlist_feature import playlist
from setup import song


class User:
    def __init__(self, playlists={}):
        self.playlists = playlists

    def add_playlist(self, name: str):
        new_playlist = playlist.Playlist(name)
        self.playlists[name] = new_playlist

    def add_song(self, playlist_name: str, new_song: song.Song):
        self.playlists.get(playlist_name).add_song(new_song)



