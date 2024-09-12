class Counter:

    def __init__(self, current: int = 1, min_value: int = 0, max_value: int = 10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

        if not (self.min_value <= self.current <= self.max_value):
            raise ValueError(f"Початкове значення повинно бути між {self.min_value} і {self.max_value}")

    def set_current(self, start):
        if self.min_value <= start <= self.max_value:
            self.current = start
        else:
            raise ValueError(f"Початкове значення повинно бути між {self.min_value} і {self.max_value}")

    def set_max(self, max_max: int):
        self.max_value = max_max
        if self.current > self.max_value:
            self.current = self.max_value

    def set_min(self, min_min):
        self.min_value = min_min
        if self.current < self.min_value:
            self.current = self.min_value

    def step_up(self):
        if self.current < self.max_value:
            self.current += 1
        else:
            raise ValueError("Досягнуто максимуму")

    def step_down(self):
        if self.current > self.min_value:
            self.current -= 1
        else:
            raise ValueError("Досягнуто мінімуму")

    def get_current(self):
        return self.current


counter = Counter()

counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()

assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()  # Очікується ValueError
except ValueError as e:
    print(e)  # "Досягнуто максимуму"

assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()

assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()  # Очікується ValueError
except ValueError as e:
    print(e)  # "Досягнуто мінімуму"

assert counter.get_current() == 7, 'Test4'