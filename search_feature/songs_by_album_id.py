from search_feature import search


class Songs_by_album_id(search.Search):
    def albums_id_by_artist_id(self, artist_id):
        albums_ids = []
        albums = self.transformer.application.artists.get(artist_id).albums
        for album in albums.values():
            albums_ids.append(album.id)
        return albums_ids

    def search(self, search_by):
        songs_names = []
        artists = self.transformer.application.artists.values()
        for artist in artists:
            all_albums_id = self.albums_id_by_artist_id(artist.id)
            if search_by in all_albums_id:
                print(all_albums_id)
                print(artist.name)
                songs = self.transformer.application.artists.get(artist.id).albums.get(search_by).songs
                for song in songs.values():
                    songs_names.append(song.name)
        return songs_names
