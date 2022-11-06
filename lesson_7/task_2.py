stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}

total_price = [stock.get(key) * prices.get(key) for key in stock]
print("The total price is", sum(total_price))
