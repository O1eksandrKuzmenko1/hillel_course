class Item:
    def __init__(self, name: str, price: int | float, description: str, dimensions: str):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self) -> str:
        return f"{self.name}, price: {self.price}"

class User:
    def __init__(self, name: str, surname: str, numberphone: str):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"

class Purchase:
    def __init__(self, user: User):
        self.products = {}
        self.user = user

    def add_item(self, item: Item, cnt: int):
        if item in self.products:
            self.products[item] += cnt
        else:
            self.products[item] = cnt

    def __str__(self) -> str:
        items_str = "\n".join([f"{item.name}: {cnt} pcs." for item, cnt in self.products.items()])
        return f"User: {self.user}\nItems:\n{items_str}"

    def get_total(self) -> int | float:
        return sum(item.price * cnt for item, cnt in self.products.items())


lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")

print(lemon)
print(apple)

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)

assert isinstance(cart.user, User), 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
cart.add_item(apple, 10)
print(cart)

assert cart.get_total() == 80, 'Повинно залишатися 80!'
