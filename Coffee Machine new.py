# variables------------------------------------------------------------------------------------------------------------
water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
money = 550
checks = True

# lists-----------------------------------------------------------------------------------------------------------------
global available
available = [water, milk, coffee_beans, disposable_cups]
ingredients = ["water", "milk", "coffee beans", "cups"]

# functions-------------------------------------------------------------------------------------------------------------


def take_action():
    global action
    action = input("Write action (buy, fill, take, remaining, exit):\n")


def def_action():

    if action == "fill":
        fill()

    elif action == "take":
        take()

    elif action == "buy":
        buy()

    elif action == "remaining":
        status()


def fill():
    global water
    global milk
    global coffee_beans
    global disposable_cups
    global money

    fill_water = int(input("Write how many ml of water you want to add:\n"))
    fill_milk = int(input("Write how many ml of milk you want to add:\n"))
    fill_beans = int(input("Write how many grams of coffee beans you want to add:\n"))
    fill_cups = int(input("Write how many disposable coffee cups you want to add:\n"))

    water += fill_water
    milk += fill_milk
    coffee_beans += fill_beans
    disposable_cups += fill_cups

    available[0] = water
    available[1] = milk
    available[2] = coffee_beans
    available[3] = disposable_cups


def take():
    global money
    print(f"I gave you ${money}")
    money = 0


def buy():
    global water
    global milk
    global coffee_beans
    global disposable_cups
    global money
    global checks
    global available

    espresso = [250, 0, 16, 1]
    latte = [350, 75, 20, 1]
    cappuccino = [200, 100, 12, 1]

    type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")

    if type == "back":
        pass

    elif type == "1":
        make(espresso)
        if checks:
            water -= 250
            coffee_beans -= 16
            disposable_cups -= 1
            money += 4

            available[0] = water
            available[2] = coffee_beans
            available[3] = disposable_cups

    elif type == "2":
        make(latte)
        if checks:
            water -= 350
            milk -= 75
            coffee_beans -= 20
            disposable_cups -= 1
            money += 7

            available[0] = water
            available[1] = milk
            available[2] = coffee_beans
            available[3] = disposable_cups

    elif type == "3":
        make(cappuccino)
        if checks:
            water -= 200
            milk -= 100
            coffee_beans -= 12
            disposable_cups -= 1
            money += 6

            available[0] = water
            available[1] = milk
            available[2] = coffee_beans
            available[3] = disposable_cups


def make(c_type):
    global checks
    global available
    validation = []

    for element in c_type:
        index = c_type.index(element)

        if element <= available[index]:
            validation.append("yes")

            if len(validation) == 4:
                print("I have enough resources, making you a coffee!")
                checks = True

        elif len(validation) != 4:
            print(f"Sorry, not enough {ingredients[c_type.index(element)]}!")
            checks = False


def status():
    print(f"""The coffee machine has:
{water} of water
{milk} of milk
{coffee_beans} of coffee beans
{disposable_cups} of disposable cups
${money} of money""")


def space():
    print(" ")


# execution ------------------------------------------------------------------------------------------------------------

while True:
    take_action()
    if action == "exit":
        break
    space()
    def_action()
    space()
