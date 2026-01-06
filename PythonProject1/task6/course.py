class Course:
    def __init__(self, title: str, teacher):
        self._title = title
        self._teacher = teacher
        self._students = []
        self._capacity = 30

    @property
    def title(self):
        return self._title

    @property
    def teacher(self):
        return self._teacher

    @property
    def students(self):
        return self._students[:]

    def add_student(self, student):
        if len(self._students) >= self._capacity:
            raise ValueError("Course is full")

        for s in self._students:
            if s.name == student.name and s.grade == student.grade:
                raise ValueError("Duplicate student")

        self._students.append(student)

    def remove_student(self, student):
        if student in self._students:
            self._students.remove(student)

    def list_students(self):
        return sorted(self._students, key=lambda s: s.name)

    def get_summary(self):
        return f"Course: {self._title}, Teacher: {self._teacher.name}, Students: {len(self._students)}"
