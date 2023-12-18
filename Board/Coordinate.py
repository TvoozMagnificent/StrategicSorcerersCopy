
from Board.util import rank, file

class Coordinate:
    """
    Coordinate immutable class
    """

    def __init__(self, r: int, f: int) -> None:
        """
        Initialize coordinate class (a coordinate)
        :param r: an integer 0~7 denoting ranks 1~8
        :param f: an integer 0~7 denoting files a~h
        """
        assert r in [0, 1, 2, 3, 4, 5, 6, 7]
        assert f in [0, 1, 2, 3, 4, 5, 6, 7]
        self.r = r
        self.f = f

    def __repr__(self):
        """
        :return: algebraic notation as in h3
        """
        return f"{file(self.f)}{rank(self.r)}"

    def __eq__(self, other):
        return self.r == other.r and self.f == other.f
