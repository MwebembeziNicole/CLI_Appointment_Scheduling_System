import json
from abc import ABC, abstractmethod

class StorageInterface(ABC):
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def save(self, data): pass


class JSONStorage(StorageInterface):
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save(self, data):
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)