class CoffeeMachine:

    # variables and lists
    water = 450
    milk = 540
    coffee_beans = 120
    disposable_cups = 9
    money = 550

    action = None
    type_coffee = None
    checks = True

    available = [water, milk, coffee_beans, disposable_cups]
    ingredients = ["water", "milk", "coffee beans", "cups"]

    # taking user input
    def user_input(self):
        self.action = input("Write action (buy, fill, take, remaining, exit):\n")

    def type_action(self):
        if __name__ == '__main__':
            if self.action == "remaining":
                CoffeeMachine.status(self)
            elif self.action == "buy":
                CoffeeMachine.buy(self)
            elif self.action == "take":
                CoffeeMachine.take(self)
            elif self.action == "fill":
                CoffeeMachine.fill(self)

    def status(self):
        print(f"\nThe coffee machine has: \n{self.water} of water \n{self.milk} of milk"
              f"\n{self.coffee_beans} of coffee beans \n{self.disposable_cups} of disposable cups "
              f"\n${self.money} of money\n")

    # belongs to method buy (self)
    def make(self, c_type):
        validation = []
        for element in c_type:
            index = c_type.index(element)

            if element <= self.available[index]:
                validation.append("yes")

                if len(validation) == 4:
                    print("I have enough resources, making you a coffee!\n")
                    self.checks = True

            elif len(validation) != 4:
                print(f"Sorry, not enough {self.ingredients[c_type.index(element)]}!\n")
                self.checks = False

    def buy(self):
        self.type_coffee = input("\nWhat do you want to buy?"
                                 " 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")

        espresso = [250, 0, 16, 1]
        latte = [350, 75, 20, 1]
        cappuccino = [200, 100, 12, 1]

        if self.type_coffee == "back":
            print("")
            pass

        elif self.type_coffee == "1":
            CoffeeMachine.make(self, c_type=espresso)
            if self.checks:
                self.water -= 250
                self.coffee_beans -= 16
                self.disposable_cups -= 1
                self.money += 4

                self.available[0] = self.water
                self.available[2] = self.coffee_beans
                self.available[3] = self.disposable_cups

        elif self.type_coffee == "2":
            CoffeeMachine.make(self, c_type=latte)
            if self.checks:
                self.water -= 350
                self.milk -= 75
                self.coffee_beans -= 20
                self.disposable_cups -= 1
                self.money += 7

                self.available[0] = self.water
                self.available[1] = self.milk
                self.available[2] = self.coffee_beans
                self.available[3] = self.disposable_cups

        elif self.type_coffee == "3":
            CoffeeMachine.make(self, c_type=cappuccino)
            if self.checks:
                self.water -= 200
                self.milk -= 100
                self.coffee_beans -= 12
                self.disposable_cups -= 1
                self.money += 6

                self.available[0] = self.water
                self.available[1] = self.milk
                self.available[2] = self.coffee_beans
                self.available[3] = self.disposable_cups

    def take(self):
        print(f"\nI gave you ${self.money}\n")
        self.money = 0

    def fill(self):
        self.water += int(input("\nWrite how many ml of water you want to add:\n"))
        self.milk += int(input("Write how many ml of milk you want to add:\n"))
        self.coffee_beans += int(input("Write how many grams of coffee beans you want to add:\n"))
        self.disposable_cups += int(input("Write how many disposable coffee cups you want to add:\n"))

        self.available[0] = self.water
        self.available[1] = self.milk
        self.available[2] = self.coffee_beans
        self.available[3] = self.disposable_cups

        print("")


def main():
    coffee = CoffeeMachine()
    while True:
        coffee.user_input()
        if coffee.action == "exit":
            break
        coffee.type_action()


if __name__ == '__main__':
    main()
