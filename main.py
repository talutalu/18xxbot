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
    states = [board.start()]

    plays = board.legal_plays(states)
    for play in plays:
        print(play)

    states.append(board.next_state(states[-1], plays[1]))

    plays = board.legal_plays(states)
    for play in plays:
        print(play)
    """board = Board()
    mc = MonteCarlo(board=board)
    mc.update(board.start())
    mc.get_play()"""
