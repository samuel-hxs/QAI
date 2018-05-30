import configparser


class Config:
    config: configparser = None
    path: str = None

    def __init__(self, path: str):
        self.path = path
        self.config = configparser.ConfigParser()
        try:
            self.config.read(path)
        except FileNotFoundError as ex:
            print(ex)
