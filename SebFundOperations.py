
import re

class SebFundOperations:
    def __init__(self):
        pass
    
    def get_interval(self, fund):
        fund_start = fund.iloc[0].name
        fund_end = fund.iloc[-1].name
        
        return fund_start, fund_end

    def filter_interval(self, funds, start, end):
        available_funds = []
        for name in funds:
            fund = funds[name]
            (fund_start, fund_end) = self.get_interval(fund)
            if start >= fund_start and end <= fund_end:
                available_funds.append(name)

        return available_funds

    # regexp
    # .*  - any alfacharacter
    # $   - end
    # ^   - start
    # SEB - All that starts with SEB 
    def filter_name(self, funds, regexp):
        filtered_funds = []
        for name in funds:
            if re.match(regexp, name):
                filtered_funds.append(name)
                
        return filtered_funds