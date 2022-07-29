# 4'50
import csv

# ? with open("data.csv", "w") as file:
# ?     writer = csv.writer(file)
# ?     writer.writerow(["transaction_id", "product_id", "price"])
# ?     writer.writerow([100, 1, 5])
# ?     writer.writerow([101, 2, 6])

# i u root-u pokraj "app.py"a se pojavio data.csv

# a sada citanje csv-fajla

with open("data.csv") as file:
    reader = csv.reader(file)
    print(list(reader))
    # [['transaction_id', 'product_id', 'price'], ['100', '1', '5'], ['101', '2', '6']]

# a potom malo loopanja

with open("data.csv") as file:
    reader = csv.reader(file)
    # print(list(reader))
    for row in reader:
        print(row)
# i dobijemo: ['transaction_id', 'product_id', 'price']; ['100', '1', '5']; ['101', '2', '6']

# u py-u je lako raditi sa csv-fajlovima, mozemo iterirati, mozemo ih kombinirati, summerize itd, kalkulirati i stornirati u drugi csv-fajl itd
