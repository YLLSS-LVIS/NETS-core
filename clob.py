from exchange_data import exchange_data as exchg_data
from market import Market
from sortedcontainers import SortedDict as sd


class clob:
    def __init__(self, _market: Market, clob_slot_idx: int):
        self.tob = [None, None]
        self.books = [sd(), sd()]
        self.userPositions = {}

        exchange_data: exchg_data = _market._exchange_data
        self.contractNotional = _market.contractNotional
        self.acctOrderLimit = exchange_data.acctMaxOrders
        self.clobSlot = clob_slot_idx

        self.tobSum = _market.tob_sum
        # [bid, offer]
        self.headClobs = [-1, -1]
        self.tailClobs = [-1, -1]
        self.marketHeadClobs = _market.head_clobs
        self.marketTailClobs = _market.tail_clobs
        self.clobList = _market.markets

        self._allocOrder = exchange_data.get_order_slot
        self._deallocOrder = exchange_data.release_order_slot
        self.orderID = exchange_data.orderID
        self.orderMarket = exchange_data.orderMarket
        self.orderOutcome = exchange_data.orderOutcome
        self.orderPrice = exchange_data.orderPrice
        self.orderSide = exchange_data.orderSide
        self.orderQty = exchange_data.orderQty
        self.orderAcctHead = exchange_data.orderAcctHead
        self.orderAcctTail = exchange_data.orderAcctTail
        self.orderClobHead = exchange_data.orderClobHead
        self.orderClobTail = exchange_data.orderClobTail

    def log_occupied_clob(self, side):
        mkt_slot = self.clobSlot
        if self.marketHeadClobs[side] == -1:
            self.marketHeadClobs[side] = mkt_slot
            self.marketTailClobs[side] = mkt_slot
            return
        current_tail = self.marketTailClobs[side]
        if current_tail == mkt_slot:
            return
        self.clobList[current_tail].tailClobs[side] = mkt_slot
        self.tailClobs[side] = -1
        self.headClobs[side] = current_tail

    def log_empty_clob(self, side):
        mkt_head = self.headClobs[side]
        mkt_tail = self.tailClobs[side]

        if mkt_head != -1:
            self.clobList[mkt_head].tailClobs[side] = mkt_tail
        else:
            self.marketHeadClobs[side] = mkt_tail
        if mkt_tail != -1:
            self.clobList[mkt_tail].headClobs[side] = mkt_head
        else:
            self.marketTailClobs[side] = mkt_head
