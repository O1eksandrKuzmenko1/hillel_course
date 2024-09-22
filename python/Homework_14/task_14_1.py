class GroupException(Exception):
    pass


class Human:
    def __init__(self, gender: str, age: int, first_name: str, last_name: str):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} years old"


class Student(Human):
    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"Student {self.first_name} {self.last_name}, {self.gender}, {self.age} years old, Record book: {self.record_book}"


class Group:
    def __init__(self, number: str):
        self.number = number
        self.group = set()

    def add_student(self, student: Student):
        self.group.add(student)
        if len(self.group) > 10:
            raise GroupException("Group size > 10")

    def delete_student(self, last_name: str):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name: str):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = "\n".join(str(student) for student in self.group)
        return f"Group {self.number}:\n{all_students}"


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')
try:
    for i in range(12):
        gr.add_student(Student('Male', i + 17, 'Vasya', 'Vasov', f'AN{i}123'))
except GroupException as ge:
    print(ge)
