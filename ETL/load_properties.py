class Loader:
    @staticmethod
    def load_properties(file_path: str, search_value: str, separator="="):
        keys = {}

        with open(file_path) as file:

            for line in file:
                if separator in line:
                    name, value = line.split(separator, 1)
                    keys[name.strip()] = value.strip()

        return keys.get(search_value)