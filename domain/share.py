from domain.company import Company


class Share:

    def __init__(self, company: Company, pct: int, is_president: bool):
        self.company = company
        self.pct = pct
        self.is_president = is_president