class Category:
    def __init__(self, title):
        self.title = title
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def __str__(self):
        return f"{'*' * 10}{self.title}{'*' * 10}\n" + '\n'.join(map(str, self.dishes))