class STUDENT:
    def __init__(self, last_name, first_name, birth_year, course, grades):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_year = birth_year
        self.course = course
        self.grades = grades
    def __del__(self):
        print(f"Student {self.first_name} {self.last_name} видалений")
    def change_grades(self, new_grades):
        self.grades = new_grades
    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0
students = [
    STUDENT("Левинець", "Іван", 2000, 3, [90, 85, 88]),
    STUDENT("Розбитиш", "Ольга", 1999, 5, [75, 80, 78]),
    STUDENT("Потихайло", "Андрій", 2001, 2, [95, 92, 91]),
    STUDENT("Репець", "Марія", 2002, 1, [65, 70, 72])
]
students_sorted = sorted(students, key=lambda student: student.average_grade(), reverse=True)
print("Відсортований список студентів за успішністю:")
for student in students_sorted:
    print(f"{student.last_name} {student.first_name} - Середній бал: {student.average_grade():.1f}")
