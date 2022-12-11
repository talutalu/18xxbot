from __future__ import annotations

from domain.state.map.tile import Tile
from service.board.board import Board
from service.montecarlo.montecarlo import MonteCarlo


def test_tile():
    tile = Tile(connections=[(1, 1), (2, 2), (4, 4), (5, 5)], level=1, cities=[])
    for t in tile.get_unique_rotations():
        print(t)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board = Board()
    state = board.start()
    future_tiles = board.legal_plays([state])
    for future_tile in future_tiles:
        print(future_tile)
    """board = Board()
    mc = MonteCarlo(board=board)
    mc.update(board.start())
    mc.get_play()"""
