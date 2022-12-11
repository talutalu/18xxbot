from domain.play.play import Play
from domain.state.map.tile import Tile


class LayTrackPlay(Play):

    def __init__(self, tile: Tile):
        self.tile = tile

    def __str__(self):
        return f"LayTrackPlay({self.tile})"
