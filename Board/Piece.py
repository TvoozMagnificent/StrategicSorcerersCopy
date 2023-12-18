
from Board.Move import Move
from Board.Coordinate import Coordinate

class Piece:
    """
    Simulates a Chess Piece
    """

    def __init__(self, coordinate: Coordinate, board) -> None:
        """
        Initialize piece class (a coordinate)
        :param coordinate: its current coordinate
        :param board: the board the current piece is in
        """
        self.coord = coordinate
        self.board = board

    def legal_moves(self) -> list[Move]:
        """
        :return: all legal moves of the piece
        """
        assert False # abstract method should be overwritten

    def move(self, coordinate: Coordinate):
        """
        Move the piece to coordinate.
        (More acurately, set self.coord of current piece to coordinate
        :param coordinate: its destination
        :return: self
        """
        self.coord = coordinate
        return self

    def __repr__(self) -> str:
        """
        :return: algebraic notation of this piece
        p and P are used. Uppercase denotes white pieces.
        """
        assert False # abstract method should be overwritten
