class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

class Settings(Singleton):
    def setup(self, **kwargs):
        self.MODEL_HOST = kwargs["MODEL_HOST"]
    
    @property
    def MODEL_HOST(self):
        return self._MODEL_HOST
    
    @MODEL_HOST.setter
    def MODEL_HOST(self, value):
        self._MODEL_HOST = value
