from exchange_data import exchange_data
from user_positions import user_positions

exchange = exchange_data(max_accounts=1, max_orders=1, max_markets=1)
positions = user_positions(_exchange_data=exchange, market_ticks=100)

exchange.create_acct(0, 1000000)
positions.post_order(0, 50, 0, 50)
positions.fill_order(0, 50, 0, 50, 50)
print(exchange.available)
print(positions.positions)
print()
positions.post_order(0, 50, 1, 101)
positions.cancel_order(0, 50, 1, 2)
print(positions.positions)
print(exchange.available)
