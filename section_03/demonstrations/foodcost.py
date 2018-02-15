class Item:

    def __init__(self, name="item", price=0, cost=0, children=[]):
        self.name = name
        self.price = price
        self.cost = cost
        self.children = children

    def get_cost(self):
        output = self.cost
        for c in self.children:
            output += c.get_cost()
        return output

    def get_profit(self):
        return self.price - self.get_cost()


cheese = Item("cheese", 0.0, 1.00)
dough = Item("dough", 0.0, 2.00)
pepperoni = Item("pepperoni", 0.0, 3.00)
# delivery = Item("delivery ", 0.0, 10.00)

labor = Item("labor", 0.0, 7.50)
beer = Item("beer", 4.00, 1.00)

pepperoni_pizza = Item("Pepperoni Pizza",
                       24.99,
                       0.0,
                       [
                           cheese,
                           dough,
                           pepperoni
                       ]
                       )

gross = 30 * 30 * pepperoni_pizza.get_profit()
gross += 30 * 200 * beer.get_profit()

all_labor = 4 * labor.get_cost() * 30 * 30

print gross
rent = 2000
utils = 500
overhead = rent + utils
net = gross - overhead - all_labor
print net
