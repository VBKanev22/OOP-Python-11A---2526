from task1.person import Person

class Teacher(Person):
    def __init__(self, name: str, age: int, subject: str):
        super().__init__(name, age)
        self._subject = subject

    @property
    def subject(self):
        return self._subject

    def get_info(self):
        return f"{super().get_info()}, Subject: {self._subject}"
