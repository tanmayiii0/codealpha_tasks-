# Stock Portfolio Tracker

# Hardcoded stock prices
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "AMZN": 200
}

total_investment = 0

print("Available Stocks:")
for stock in stocks:
    print(stock, ":", stocks[stock])

# Number of stocks user wants to buy
n = int(input("\nHow many stocks do you want to enter? "))

for i in range(n):
    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stocks:
        investment = stocks[stock_name] * quantity
        total_investment += investment
        print("Investment for", stock_name, "=", investment)

    else:
        print("Stock not available!")

print("\nTotal Investment Value =", total_investment)

# Optional file saving
file = open("portfolio.txt", "w")
file.write("Total Investment Value = " + str(total_investment))
file.close()

print("Result saved in portfolio.txt")
