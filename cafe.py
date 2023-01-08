# list of items
menu = ['coffee', 'sugar', 'hot chocolate','milk']

# dictionary of no. of items in stock
# list of stock values
stock = {menu[0] : 12,
         menu[1] : 21,
         menu[2] : 7,
         menu[3] : 31
        }
print(stock)
stock_value = [i for i in stock.values()]


# dictionary of price of each item in stock
# list of price values
price = {menu[0] : 3.55,
         menu[1] : 0.79,
         menu[2] : 1.30,
         menu[3] : 1.25
         }
print(price)
stock_price = [i for i in price.values()]


# calculate total price of each the item
# total of all the stocked items
c = stock_price[0] * stock_value[0]
s = stock_price[1] * stock_value[1]
hc = stock_price[2] * stock_value[2]
m = stock_price[3] * stock_value[3]

total_stock = c + s + hc + m
print("GBP", round(total_stock, 2))  # rounded to 2d.p.








