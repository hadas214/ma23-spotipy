import operator

from search_feature import search
from ETL import load_properties


class Top10_by_artist_id(search.Search):
    def search(self, search_by):
        songs_names = {}
        albums = self.transformer.application.artists.get(search_by).albums
        for album in albums.values():
            songs = album.songs
            for song in songs.values():
                print(song.name)
                songs_names[song.popularity] = song
        sort_songs_by_popularity = dict(sorted(songs_names.items(), key=operator.itemgetter(0), reverse=True))
        limit_songs = load_properties.Loader.load_properties(self.property_file, "limit.songs")
        limit_songs = int(limit_songs)
        top10_songs = dict(list(sort_songs_by_popularity.items())[:limit_songs])
        return top10_songs


s = Top10_by_artist_id()
print(s.search("3EOEK57CV77D4ovYVcmiyt"))
