
from Board.Piece import Piece
from Board.Move import Move

class Nulce(Piece):
    """
    This is a null piece that acts like the blank
    """

    def legal_moves(self) -> list[Move]:
        assert False # Nulce should never be called with legal_moves

    def __repr__(self) -> str:
        return " "
