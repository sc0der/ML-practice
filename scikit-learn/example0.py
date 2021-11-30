from sklearn import datasets

house_prices = datasets.load_digits()
print(house_prices.images[4])
