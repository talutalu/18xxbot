from __future__ import annotations

from service.board.board import Board
from service.montecarlo.montecarlo import MonteCarlo


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """board = Board()
    states = [board.start()]

    plays = board.legal_plays(states)
    for play in plays:
        print(play)

    states.append(board.next_state(states[-1], plays[1]))

    plays = board.legal_plays(states)
    for play in plays:
        print(play)"""
    board = Board()
    mc = MonteCarlo(board=board)
    mc.update(board.start())
    mc.get_play()
