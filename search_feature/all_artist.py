from search_feature import search


class All_artist(search.Search):
    def search(self, search_by):
        artists_names = []
        artists = self.transformer.application.artists.values()
        for artist in artists:
            artists_names.append(artist.name)
        return artists_names
