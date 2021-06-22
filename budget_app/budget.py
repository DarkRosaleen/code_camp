class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []

    def get_balance(self):
        total = 0
        for items in self.ledger:
            item = items["amount"]
            total = total + item
        return total

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount) is False:
            return False
        else:
            self.ledger.append({"amount": -amount, "description": description})
            return True

    def transfer(self, amount, category):
        if self.check_funds(amount) is False:
            return False
        else:
            self.withdraw(amount, "Transfer to " + category.category)
            category.deposit(amount, "Transfer from " + self.category)
            return True

    def __str__(self):
        first_title = "*" * ((30 - len(self.category)) // 2) + self.category
        final_title = first_title + "*" * (30 - len(first_title)) + "\n"

        details = ""
        for items in self.ledger:
            amount = "{:.2f}".format(items["amount"])[:7]
            description = items["description"][:23]
            details += description + amount.rjust(30 - len(description)) + "\n"
        total = "Total: " + "{:.2f}".format(self.get_balance())
        return final_title + details + total


def create_spend_chart(categories):
    bar_chart = []
    title = "Percentage spent by category"
    bar_chart.append(title)

    bars = []
    labels = [(str(p) + "| ").rjust(5) for p in range(0, 110, 10)]
    labels.reverse()
    bars.append(labels)

    withdrawals = []
    for category in categories:
        withdrawn = 0
        for obj in category.ledger:
            if obj["amount"] < 0:
                withdrawn += obj["amount"]
        withdrawals.append(withdrawn)

    percentages = []
    for w in withdrawals:
        p = w / sum(withdrawals) * 100
        # Round down to the nearest 10
        p = int(p - (p % 10))
        percentages.append(p)

    for p in percentages:
        bar = ["o  " for _ in range(0, p + 10, 10)]
        bar += ["   "] * (len(labels) - len(bar))
        bar.reverse()
        bars.append(bar)

    len_labels = len(labels)
    num_categories = len(categories)
    for i in range(len_labels):
        line = ""
        for j in range(num_categories + 1):
            line += bars[j][i]
        bar_chart.append(line)

    len_barchart_line = len(bar_chart[1])
    hor = ("-" * 3 * num_categories + "-").rjust(len_barchart_line)
    bar_chart.append(hor)

    names = [category.category for category in categories]
    longest_name = len(max(names, key=len))
    names = [name + " " * (longest_name - len(name)) for name in names]

    for i in range(longest_name):
        line = ""
        for j in range(num_categories):
            line += names[j][i] + "  "
        bar_chart.append(line.rjust(len_barchart_line))

    return "\n".join(bar_chart)
