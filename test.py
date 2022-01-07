import math

# user input
water_in = int(input("Write how many ml of water the coffee machine has:\n"))
milk_in = int(input("Write how many ml of milk the coffee machine has:\n"))
beans_in = int(input("Write how many grams of coffee beans the coffee machine has:\n"))
cups = int(input("Write how many cups of coffee you will need:\n"))

# ingredients
water = math.floor(water_in / 200)
milk = math.floor(milk_in / 50)
beans = math.floor(beans_in / 15)

# lowest number of cups of coffee
number_cups = [water, milk, beans]
lowest = min(number_cups)

# if statements
if lowest == cups:
    print("Yes, I can make that amount of coffee")

elif lowest > cups:
    additional = lowest - cups
    print(f"Yes, I can make that amount of coffee (and even {additional} more than that)")

else:
    print(f"No, I can make only {lowest} cups of coffee")