from .bumpy_sole import BumpySole
from .round_shoe_lace import RoundShoeLace
from .shoe_factory import ShoeFactory
from .shoe_lace import ShoeLace
from .sole import Sole


class SportsShoeFactory(ShoeFactory):
    """Concrete Factory for sports shoes"""

    def create_sole(self) -> Sole:
        return BumpySole()

    def create_shoe_lace(self) -> ShoeLace:
        return RoundShoeLace()
