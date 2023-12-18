
from Board.Piece import Piece
from Board.White import White
from Board.Black import Black
from Board.Nulce import Nulce

from Board.Coordinate import Coordinate
from Board.Move import Move

class Rook(Piece):
    """
    This is a demo piece that acts like the rook
    """

    def legal_moves(self):
        moves = []
        for dr, df in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ri = self.coord.r
            fi = self.coord.f
            while True:
                ri += dr
                fi += df
                try: coord = Coordinate(ri, fi)
                except: break
                _ = self.board.get_square(coord)
                if not isinstance(_, Nulce):
                    if isinstance(self, White) and isinstance(_, White): break
                    if isinstance(self, Black) and isinstance(_, Black): break
                moves.append(Move(self, coord))
                if not isinstance(_, Nulce): break
        return moves

    def __repr__(self):
        return 'R' if isinstance(self, White) else 'r'

class WhiteRook(White, Rook): pass
class BlackRook(Black, Rook): pass
