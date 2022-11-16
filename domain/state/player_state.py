from domain.share import Share
from domain.company import Company
from domain.player import Player


class PlayerState:

    def __init__(self, player: Player, money: int, shares: list[Share]):
        self.player = player
        self.money = money
        self.shares = shares
