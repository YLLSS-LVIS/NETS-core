class Market:
    def __init__(self, userID, n_outcomes, mkt_ticks):
        self.nOutcomes = n_outcomes
        self.mkt_ticks = mkt_ticks
        self.userPositions = {}
