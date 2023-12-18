
from Board.Move import Move
from Board.Coordinate import Coordinate

from Board.Nulce import Nulce as NN
from Board.Rook import WhiteRook as WR, BlackRook as BR
from Board.Knight import WhiteKnight as WN, BlackKnight as BN
from Board.Bishop import WhiteBishop as WB, BlackBishop as BB
from Board.Queen import WhiteQueen as WQ, BlackQueen as BQ
from Board.King import WhiteKing as WK, BlackKing as BK
from Board.Soldier import WhiteSoldier as WS, BlackSoldier as BS

from Board.White import White
from Board.Black import Black

class Board:
    """
    Board class

    Simulates a board with all history states remembered.
    """

    def __init__(self) -> None:
        """
        Initializes starting grid
        """
        _ = [
            [BR, BN, BB, BQ, BK, BB, BN, BR],
            [BS, BS, BS, BS, BS, BS, BS, BS],
            [NN, NN, NN, NN, NN, NN, NN, NN],
            [NN, NN, NN, NN, NN, NN, NN, NN],
            [NN, NN, NN, NN, NN, NN, NN, NN],
            [NN, NN, NN, NN, NN, NN, NN, NN],
            [WS, WS, WS, WS, WS, WS, WS, WS],
            [WR, WN, WB, WQ, WK, WB, WN, WR],
        ]
        for i in range(8):
            for j in range(8):
                _[i][j] = _[i][j](Coordinate(i, j), self)
        self.state = _
        self.player = White
        self.available_moves = self.all_moves()

    def all_moves(self):
        moves = []
        for _ in self.state:
            for piece in _:
                if isinstance(piece, self.player):
                    moves += piece.legal_moves()
        return moves

    def move(self, move: Move) -> bool:
        """
        Push move into state history
        More specifically,
        move move.piece to move.dest and clear
        move.start

        then, switch self.player

        :param move: Move being made
        :return: True if game decided (self.player loses), False o.w.
        """
        assert move in self.available_moves # Illegal Move
        self.set_square(move.dest, move.piece.move(move.dest))
        self.empty_square(move.start)
        if self.player == White: self.player = Black
        else: self.player = White
        self.available_moves = self.all_moves()
        return self.available_moves == [] # o.w. one player has won

    def get_square(self, coord: Coordinate):
        """
        :param coord: Coordinate of a square
        :return: The square at coordinates coord
        """
        return self.state[coord.r][coord.f]

    def set_square(self, coord: Coordinate, piece):
        """
        :param coord: Coordinate of a square
        :param piece: Piece to set
        :return: piece
        """
        self.state[coord.r][coord.f] = piece
        return piece

    def empty_square(self, coord: Coordinate):
        """
        alias for self.set_square(coord, Nulce(coord, self))
        :param coord: Coordinate of a square
        :return: the Nulce created
        """
        return self.set_square(coord, NN(coord, self))

    def __repr__(self) -> str:
        """
        :return: ASCII representation of the board
        """
        return '\n'.join([' '.join([str(p) for p in j]) for j in self.state])
