from ETL import load_properties
from ETL import convetor
from ETL import reader_file


def main():
    # load property, search after value that called folder.songs in the property
    folder = load_properties.Loader.load_properties('C:\ma23\Spotipy\properties.properties', 'folder.songs')

    # read the folder that contains all the json files and load them
    r = reader_file.Reader()

    c = convetor.Convetor()
    data = r.parse(folder)
    c.parse(data)


if __name__ == '__main__':
    main()