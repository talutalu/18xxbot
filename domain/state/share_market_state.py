from domain.company import Company
from domain.state.company_state import CompanyState


class ShareMarketState:

    def __init__(self):
        # simple linear market
        self.values = [50, 60, 70, 80, 90, 100, 120, 140, 160, 180, 200, 250, 300, 350]
        self.companies: list[list[CompanyState]] = [[] for c in self.values]

    def add_company(self, company_state: CompanyState):
        index = self.values.index(company_state.share_value)
        self.companies[index].append(company_state.company)

    def move_company_left(self, company_state: CompanyState):
        index = self.values.index(company_state.share_value)
        if index == 0:
            return
        self.companies[index].remove(company_state)
        index -= 1
        company_state.share_value = self.values[index]
        self.companies[index].append(company_state)

    def move_company_right(self, company_state: CompanyState):
        index = self.values.index(company_state.share_value)
        if index == len(self.values) - 1:
            return
        self.companies[index].remove(company_state)
        index += 1
        company_state.share_value = self.values[index]
        self.companies[index].append(company_state)

    def get_companies_desc(self):
        result: list[CompanyState] = []
        for i in reversed(range(len(self.values))):
            result.extend(self.companies[i])
        return result

