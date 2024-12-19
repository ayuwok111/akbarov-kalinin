def stock_trading():
    prices = []
    
    while True:
        price = int(input())
        if price == 0:
            break
        prices.append(price)
    
    if len(prices) < 2:
        return
    buy_price = None
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]: 
            buy_price = prices[i - 1]
            break
    
    if buy_price is None:
        return 

    sell_price = None
    for i in range(i, len(prices)):
        if prices[i] < prices[i - 1]: 
            sell_price = prices[i]
            break
    
    if sell_price is None:
        return 

    profit = sell_price - buy_price

    print(buy_price, sell_price, profit)

stock_trading()
