
from Board.Piece import Piece
from Board.White import White
from Board.Black import Black
from Board.Nulce import Nulce

from Board.Coordinate import Coordinate
from Board.Move import Move

class Soldier(Piece):
    """
    This is a demo piece that acts like the rook
    """

    def __init__(self, *args, **kwargs):
        Piece.__init__(self, *args, **kwargs)
        self.direction = 1 if isinstance(self, White) else -1

    def legal_moves(self):
        moves = []
        for dr, df in [[self.direction, 0]]:
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
                break
        return moves

    def move(self, coordinate):
        if coordinate.r in [0, 7]: self.direction = -self.direction
        return Piece.move(self, coordinate)

    def __repr__(self):
        return 'S' if isinstance(self, White) else 's'

class WhiteSoldier(White, Soldier): pass
class BlackSoldier(Black, Soldier): pass
