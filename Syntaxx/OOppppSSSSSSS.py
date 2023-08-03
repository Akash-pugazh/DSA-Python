from typing import List, Any


class Student:
    def __init__(self, name: str, age: int, marks: int) -> None:
        self.name = name
        self.age = age
        self.marks = marks
        print("-----Object SuccessFully Instantiated-----")

    def get_details(self) -> None:
        return f"Name : {self.name}\nAge : {self.age}"

    def set_details(self, name: str, age: int, marks: int) -> None:
        self.name = name
        self.age = age
        self.marks = marks

    def get_marks(self) -> int:
        return self.marks


class Course:
    def __init__(self, course_name: str, maximum_students: int) -> None:
        self.course_name = course_name
        self.maximum_students = maximum_students
        self.students: List[Any] = []

    def add_student(self, student: Student) -> bool:
        if self.maximum_students != 0:
            self.students.append(student)
            self.maximum_students -= 1
            return True
        return False

    def average_of_course(self) -> int:
        value: int = 0
        for student in self.students:
            value += student.get_marks()
        return value / len(self.students)


akash = Student("Akash", 18, 90)
pugazh = Student("Pugazh", 19, 85)
virus = Student("Virus", 20, 80)

btech = Course("Btech", 2)
btech.add_student(akash)
btech.add_student(pugazh)
print(btech.students)
btech.add_student(virus)
print(btech.students)