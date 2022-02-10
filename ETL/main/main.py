from ETL import load_properties
from ETL import transform
from ETL import reader_file


def main():
    # load property, search after value that called folder.songs in the property
    folder = load_properties.Loader.load_properties(r'C:\ma23\Spotipy\properties.properties', 'folder.songs')

    # read the folder that contains all the json files and load them
    r = reader_file.Reader()

    c = transform.Transform()
    data = r.parse(folder)
    c.parse(data)
    # print(c.application.artists.keys())
    print(c.application.artists.get('6uQl3gu1AIXyvqCAxnc2q4').name)
    albums1 = c.application.artists.get('6uQl3gu1AIXyvqCAxnc2q4').albums
    for b in albums1.values():
        print(b.name)
    print(c.application.artists.get('1IAEef07H0fd9aA8aUHUlL').name)
    print(c.application.artists.get('1IAEef07H0fd9aA8aUHUlL').albums)
    albums2 = c.application.artists.get('1IAEef07H0fd9aA8aUHUlL').albums
    for b in albums2.values():
        print(b.name)


if __name__ == '__main__':
    main()