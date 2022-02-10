from ETL import config_parser
from setup import song, album, artist, spotipy


class Transform(config_parser.Parser):
    def __init__(self):
        self.application = spotipy.Spotipy()

    def parse(self, parse_value):
        for file in parse_value:
            information = file.get("track")

            song_id = information.get("id")
            song_name = information.get("name")
            song_popularity = int(information.get("popularity"))
            current_song = song.Song(song_name, song_id, song_popularity)

            album_values = information.get("album")
            album_id = album_values.get("id")
            album_name = album_values.get("name")
            current_album = album.Album(album_id, album_name)

            artists = information.get("artists")
            for item in artists:
                artist_id = item.get("id")
                artist_name = item.get("name")

                # For case if the artist is already exists in storage (self.application)
                if artist_id in self.application.artists.keys():
                    # Need to check if it is new album or the album is already exists
                    if not self.application.artists.get(artist_id).check_album(current_album):
                        self.application.artists.get(artist_id).add_album(current_album)
                    self.application.artists.get(artist_id).albums.get(current_album.id).add_song(current_song)
                else:
                    new_song = {}
                    new_song[current_song.id] = current_song
                    current_album1 = album.Album(album_id, album_name, new_song)
                    new_album = {}
                    new_album[current_album.id] = current_album1
                    current_artist = artist.Artist(artist_id, artist_name, new_album)
                    self.application.add_artist(current_artist)
                    # print(self.application.artists.get(artist_id).albums)

