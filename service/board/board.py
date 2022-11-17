from domain.share import Share
from domain.company import Company
from domain.player import Player
from domain.state.company_state import CompanyState
from domain.state.map_state import MapState
from domain.state.player_state import PlayerState
from domain.state.share_market_state import ShareMarketState
from domain.state.state import State
from domain.state.track_market_state import TrackMarketState


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
        return State(map_state=MapState.generate_test_for_2p(17, 20),
                     player_states=[player_state_a, player_state_b],
                     company_states=[company_state_1, company_state_2],
                     track_market_state=TrackMarketState(),
                     share_market_state=share_market_state)

    def current_player(self, state):
        return state.current_player()

    def next_state(self, state, play):
        # Takes the game state, and the move to be applied.
        # Returns the new game state.
        pass

    def legal_plays(self, state_history: list[State]):
        return state_history[-1].legal_plays()

    def winner(self, state_history):
        # Takes a sequence of game states representing the full
        # game history.  If the game is now won, return the player
        # number.  If the game is still ongoing, return zero.  If
        # the game is tied, return a different distinct value, e.g. -1.
        pass