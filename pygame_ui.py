
import pygame

from Board.Coordinate import Coordinate
from Board.Board import Board
from Board.Move import Move
from Board.util import id

board = Board()

while True:
    print("\n" * 100)
    print(board)
    print(f"{str(board.player)[14:][:5]} to move")
    while True:
        move = input().strip()
        try:
            result = board.move(
                Move(
                    board.get_square(Coordinate(id(int(move[1])), id(move[0]))),
                    Coordinate(id(int(move[3])), id(move[2]))
                )
            )
        except:
            print("Illegal move")
            continue
        break
    if result: print(f"{str(board.player)[14:][:5]} lost"); break
