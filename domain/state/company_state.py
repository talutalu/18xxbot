from domain.company import Company
from domain.player import Player
from domain.train import Train


class CompanyState:

    def __init__(self,
                 company: Company,
                 money: int,
                 trains: list[Train],
                 share_value: int,
                 token_location: tuple[int, int, int]):
        self.company = company
        self.money = money
        self.trains = trains
        self.share_value = share_value
        self.token_location = token_location

