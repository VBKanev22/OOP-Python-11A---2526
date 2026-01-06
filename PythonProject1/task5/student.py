from task5.person import Person

class Student(Person):
    def __init__(self, name: str, age: int, grade: int, school: str):
        super().__init__(name, age)
        if not (1 <= grade <= 12):
            raise ValueError("Invalid grade")
        self._grade = grade
        self._school = school

    @property
    def grade(self):
        return self._grade

    @property
    def school(self):
        return self._school

    def get_info(self):
        base = super().get_info()
        return f"{base}, Grade: {self._grade}, School: {self._school}"
