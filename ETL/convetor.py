from ETL import config_parser
from setup import song, album, artist


class Convetor(config_parser.Parser):
    def __init__(self):
        self.artists = {}

    def parse(self, parse_value):

        for file in parse_value:
            information = file.get("track")

            artists = information.get("artists")
            for a in artists:
                song_id = information.get("id")
                song_name = information.get("name")
                song_popularity = int(information.get("popularity"))
                my_song = song.Song(song_id, song_name, song_popularity)

                album_values = information.get("album")
                album_id = album_values.get("id")
                album_name = album_values.get("name")
                my_album = album.Album(album_id, album_name)
                my_album.add_song(my_song)

                artist_id = a.get("id")
                artist_name = a.get("name")
                my_artist = artist.Artist(artist_id, artist_name)
                my_artist.add_album(my_album.name)

                print(my_artist.albums)
