from domain.play.lay_track_play import LayTrackPlay
from domain.play.play import Play
from domain.share import Share
from domain.company import Company
from domain.player import Player
from domain.state.company_state import CompanyState
from domain.state.map.tile import Tile
from domain.state.map_state import MapState
from domain.state.player_state import PlayerState
from domain.state.share_market_state import ShareMarketState
from domain.state.state import State
from domain.state.tile_market_state import TileMarketState


class Board:

    def start(self):
        # Returns a representation of the starting state of the game.
        company_1 = Company("corp 1")
        company_state_1 = CompanyState(company_1, 200, [], 100, (8, 0, 1))
        company_2 = Company("corp 2")
        company_state_2 = CompanyState(company_2, 200, [], 100, (8, 0, 0))
        player_a = Player("bot a")
        player_b = Player("bot b")
        player_state_a = PlayerState(player_a, 20, [Share(company_1, 100, True)])
        player_state_b = PlayerState(player_b, 30, [Share(company_2, 100, True)])
        share_market_state = ShareMarketState()
        share_market_state.add_company(company_state_1)
        share_market_state.add_company(company_state_2)
        tile_market_state = TileMarketState(tiles=[
            Tile(id=0, connections=[(0, 3)], level=1, cities=[]),
            Tile(id=0, connections=[(0, 2)], level=1, cities=[]),
        ], quantities=[
            5,
            5
        ])
        return State(map_state=MapState.generate_test_for_2p(17, 20),
                     player_states=[player_state_a, player_state_b],
                     company_states=[company_state_1, company_state_2],
                     tile_market_state=tile_market_state,
                     share_market_state=share_market_state)

    def current_player(self, state):
        print("board::current_player")
        return state.current_player()

    def next_state(self, state: State, play: Play):
        print("board::next_state")
        print("  " + str(play))
        # Takes the game state, and the move to be applied.
        # Returns the new game state.

        # TODO copy state here
        state = state.clone()
        state.do_play(play)

        return state

    def legal_plays(self, state_history: list[State]):
        print("board::legal_plays")
        legal_plays = state_history[-1].legal_plays()
        for legal_play in legal_plays:
            print("  " + str(legal_play))
        return legal_plays

    def winner(self, state_history):
        print("board::winner")
        # Takes a sequence of game states representing the full
        # game history.  If the game is now won, return the player
        # number.  If the game is still ongoing, return zero.  If
        # the game is tied, return a different distinct value, e.g. -1.
        pass