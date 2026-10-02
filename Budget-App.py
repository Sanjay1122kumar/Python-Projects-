class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        output = self.name.center(30, '*') + '\n'
        for item in self.ledger:
            description = item['description'][:23]
            amount = f"{item['amount']:.2f}"[:7]
            output += f"{description:<23}{amount:>7}\n"
        output += f"Total: {self.get_balance():.2f}"
        return output


def create_spend_chart(categories):
    # Total withdrawn per category (withdrawals only)
    spent = []
    for category in categories:
        total = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        spent.append(total)

    total_spent = sum(spent)

    # Percentage of total spending, rounded down to the nearest 10
    if total_spent == 0:
        percentages = [0 for _ in spent]
    else:
        percentages = [int(s / total_spent * 100) // 10 * 10 for s in spent]

    lines = ['Percentage spent by category']

    # Bars
    for level in range(100, -1, -10):
        row = f"{level:>3}|" + " "
        row += "  ".join('o' if p >= level else ' ' for p in percentages)
        row += "  "
        lines.append(row)

    # Horizontal line
    lines.append("    " + "-" * (3 * len(categories) + 1))

    # Vertical names
    names = [category.name for category in categories]
    longest = max(len(name) for name in names) if names else 0
    for i in range(longest):
        row = "    " + " "
        row += "  ".join(name[i] if i < len(name) else ' ' for name in names)
        row += "  "
        lines.append(row)

    return "\n".join(lines)


# Example usage
if __name__ == "__main__":
    food = Category('Food')
    food.deposit(1000, 'initial deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')
    clothing = Category('Clothing')
    food.transfer(50, clothing)
    print(food)

    auto = Category('Auto')
    clothing.deposit(200, 'deposit')
    auto.deposit(100, 'deposit')
    clothing.withdraw(40, 'shirts')
    auto.withdraw(30, 'gas')
    print(create_spend_chart([food, clothing, auto]))