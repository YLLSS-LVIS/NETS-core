import array


class exchange_data:
    def __init__(self, max_accounts, max_orders, max_markets):
        acct_default = [-1 for i in range(0, max_accounts)]
        # account status
        # -1 = no account at this slot
        # 1 = activated trading account at this slot
        self.acctStatus = array.array("b", acct_default)
        # account balance/avbl.balance, head order (for tracking the list of orders in an account)
        self.balance = array.array("i", acct_default)
        self.available = array.array("i", acct_default)
        self.acctHeadOrder = array.array("i", acct_default)

        order_default = [-1 for i in range(0, max_orders)]
        self.orderID = array.array("i", [i for i in range(0, max_orders)])
        self.orderMarket = array.array("i", order_default)
        self.orderOutcome = array.array("h", order_default)
        self.orderPrice = array.array("i", order_default)
        self.orderSide = array.array("b", order_default)
        self.orderQty = array.array("i", order_default)
        self.orderAcctHead = array.array("i", order_default)
        self.orderAcctTail = array.array("i", order_default)
        self.orderClobHead = array.array("i", order_default)
        self.orderClobTail = array.array("i", order_default)

        self.markets = [None for i in range(0, max_markets)]

    def create_acct(self, acct_slot, initial_balance):
        if self.acctStatus[acct_slot] == -1:
            initial_balance = int(initial_balance)
            self.balance[acct_slot] = initial_balance
            self.available[acct_slot] = initial_balance
            self.acctStatus[acct_slot] = 1
