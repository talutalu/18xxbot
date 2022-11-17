from domain.play.lay_track_play import LayTrackPlay
from domain.state.company_state import CompanyState
from domain.state.map_state import MapState
from domain.state.player_state import PlayerState
from domain.state.share_market_state import ShareMarketState
from domain.state.track_market_state import TrackMarketState


class State:

    op_plays = [
        "lay_or_upgrade_track",
        "lay_extra_yellow_track",
        "run_trains",
        "pay_dividends",
        "buy_train"
    ]

    def __init__(self,
                 map_state: MapState,
                 player_states: list[PlayerState],
                 company_states: list[CompanyState],
                 track_market_state: TrackMarketState,
                 share_market_state: ShareMarketState,
                 phase: int = 0):
        self.map_state = map_state
        self.player_states = player_states
        self.company_states = company_states
        self.track_market_state = track_market_state
        self.share_market_state = share_market_state
        self.phase = phase

        # we suppose we start the game with the first OP, the first player is the one owning the company with
        # the highest share
        self.companies2run = self.share_market_state.get_companies_desc()
        self.op_index = 0

    def current_player(self):
        company2run = self.companies2run[0]
        for player_state in self.player_states:
            for share in player_state.shares:
                if share.is_president and share.company == company2run:
                    return player_state.player

    def legal_plays(self):
        company2run = self.companies2run[0]
        if self.op_index == 0:
            # lay_or_upgrade_track
            return [LayTrackPlay(tile) for tile in self.map_state.legal_new_tiles(company2run)]