from abc import ABC, abstractmethod

from .shoe_lace import ShoeLace
from .sole import Sole


class ShoeFactory(ABC):
    """Abstract Factory for creating shoe components"""

    @abstractmethod
    def create_shoe_lace(self) -> ShoeLace:
        pass

    @abstractmethod
    def create_sole(self) -> Sole:
        pass
