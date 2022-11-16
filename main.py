from domain.tile import Tile
from service.board.board import Board
from service.montecarlo.montecarlo import MonteCarlo


def test_tile():
    tile = Tile(connections=[(1, 1), (2, 2), (4, 4), (5, 5)], level=1, city_level=0, city_connections=[])
    for t in tile.get_unique_rotations():
        print(t)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board = Board()
    mc = MonteCarlo(board=board)
    mc.update(board.start())
    mc.get_play()
