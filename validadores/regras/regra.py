from abc import ABC, abstractmethod


class Regra(ABC):
    @abstractmethod
    def is_valid(self):
        pass
