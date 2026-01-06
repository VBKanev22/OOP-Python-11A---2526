class Person:
    def __init__(self, name: str, age: int):
        if not (0 <= age <= 120):
            raise ValueError("Invalid age")
        self._name = name
        self._age = age

    def get_info(self):
        return f"Name: {self._name}, Age: {self._age}"

    def birthday(self):
        if self._age < 120:
            self._age += 1
