from search_feature import search


class Album_by_artist_id(search.Search):
    def search(self, search_by):
        albums_names = []
        albums = self.transformer.application.artists.get(search_by).albums
        for album in albums.values():
            albums_names.append(album.name)
        return albums_names



