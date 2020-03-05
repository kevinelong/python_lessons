# BASELINE STOCK PRICE LISTING APPLICATION


class Stock():
    def __init__(self, ticker_symbol):
        self.ticker_symbol = ticker_symbol
        self.historical_quotes = []

    def moving_average(self):
        pass


class Quote():
    def __init__(self, closing_price, quote_date):
        self.closing_price = closing_price
        self.quote_date = quote_date


class StocksModel():
    stocks = {}

    def load(self, data):

        for record in data:
            date = record[0]
            symbol = record[1]
            price = record[2]

            if symbol not in self.stocks:
                self.stocks[symbol] = Stock(symbol)

            stock = self.stocks[symbol]
            quote = Quote(price, date)
            stock.historical_quotes.append(quote)


class StocksView():

    def render(self, stocks):

        for k in stocks.keys():
            print(k)
            v = stocks[k]
            previous = None
            prices = []
            for q in v.historical_quotes:
                #HOW CAN WE PRINT THE DIFFERENCE BETWEEN THIS PRICE AND THE PREVIOUS PRICE
                prices.append(q.closing_price)

                if not previous == None:
                    delta = q.closing_price - previous
                else:
                    delta = 0

                if delta > 0:
                    arrow = "^"
                elif delta < 0:
                    arrow = "v"
                else:
                    arrow = "="

                print(q.quote_date + " " + str(q.closing_price) + " " + arrow + " " + str(delta))
                previous = q.closing_price

            avg = sum(prices) / len(v.historical_quotes)

            print("historical average: %.3f" % avg)



# RAW TEST DATA
test_data = [
    ["2014-06-01", "APPL", 100.11],
    ["2014-06-02", "APPL", 110.61],
    ["2014-06-03", "APPL", 120.22],
    ["2014-06-04", "APPL", 100.54],
    ["2014-06-01", "MSFT", 20.46],
    ["2014-06-02", "MSFT", 21.25],
    ["2014-06-03", "MSFT", 32.53],
    ["2014-06-04", "MSFT", 40.71],
]

model = StocksModel()
model.load(test_data)

view = StocksView()
view.render(model.stocks)