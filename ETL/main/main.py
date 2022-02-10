from ETL import load_properties
from ETL import transform
from ETL import reader_file
from playlist_feature import playlist, user


def main():
    # load property, search after value that called folder.songs in the property
    folder = load_properties.Loader.load_properties(r'C:\ma23\Spotipy\properties.properties', 'folder.songs')

    # read the folder that contains all the json files and load them
    r = reader_file.Reader()

    c = transform.Transform()
    data = r.parse(folder)
    c.parse(data)
    # print(c.application.artists.keys())

    # print specific name of artist by artist_id
    print(c.application.artists.get('6uQl3gu1AIXyvqCAxnc2q4').name)

    hadas_user = user.User()
    hadas_user.add_playlist("pop")
    print(hadas_user.playlists)

    # print all the songs of this artist
    albums = c.application.artists.get('6uQl3gu1AIXyvqCAxnc2q4').albums
    for album in albums.values():
        for element in album.songs.values():
            hadas_user.add_song("pop", element)

    # print specific name of artist by artist_id
    print(c.application.artists.get("5BtHciL0e0zOP7prIHn3pP").name)
    print(c.application.artists.get("5BtHciL0e0zOP7prIHn3pP").albums)
    # print all the songs of this artist
    albums = c.application.artists.get("5BtHciL0e0zOP7prIHn3pP").albums
    for album in albums.values():
        for element in album.songs.values():
            hadas_user.add_song("pop", element)

    playlists = hadas_user.playlists.get("pop")
    print(playlists.songs)
    for p in playlists.songs:
        print(p.name)


if __name__ == '__main__':
    main()
