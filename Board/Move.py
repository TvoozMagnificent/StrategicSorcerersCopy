
from Board.Coordinate import Coordinate

class Move:
    """
    Class that designates a move.

    Castling is represented by the king moving two squares

    En Passant is designated by the diagonal movement
    of the capturing pawn.
    """

    def __init__(self, piece, dest: Coordinate) -> None:
        """
        Initializes a Move object representing the move
        moving piece to dest.
        :param piece: Piece that is moving
        :param dest: Destination of piece
        """
        self.start = piece.coord
        self.dest = dest
        self.piece = piece

    def __repr__(self) -> str:
        """
        :return: the move in explicit algebraic notation
        """
        return f"{self.piece}{self.start}{self.dest}"

    def __eq__(self, other):
        return self.start == other.start and self.dest == other.dest
