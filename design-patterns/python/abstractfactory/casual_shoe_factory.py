from .flat_sole import FlatSole
from .round_shoe_lace import RoundShoeLace
from .shoe_factory import ShoeFactory
from .shoe_lace import ShoeLace
from .sole import Sole


class CasualShoeFactory(ShoeFactory):
    """Concrete Factory for casual shoes"""

    def create_sole(self) -> Sole:
        return FlatSole()

    def create_shoe_lace(self) -> ShoeLace:
        return RoundShoeLace()
