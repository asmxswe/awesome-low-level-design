from .shoe_factory import ShoeFactory
from .shoe_lace import ShoeLace
from .sole import Sole
from .tape_shoe_lace import TapeShoeLace
from .thin_sole import ThinSole


class FormalShoeFactory(ShoeFactory):
    """Concrete Factory for formal shoes"""

    def create_sole(self) -> Sole:
        return ThinSole()

    def create_shoe_lace(self) -> ShoeLace:
        return TapeShoeLace()
