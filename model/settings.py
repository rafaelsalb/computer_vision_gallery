class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

class Settings(Singleton):
    def setup(self, **kwargs):
        self.API_HOST = kwargs["API_HOST"]
    
    @property
    def API_HOST(self):
        return self._API_HOST
    
    @API_HOST.setter
    def API_HOST(self, value):
        self._API_HOST = value
