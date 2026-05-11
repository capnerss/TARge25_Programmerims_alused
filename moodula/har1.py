class Course:
    def __init__(self, name, max_students):
        self.name = name

    def get_grades(self):
        pass

    def get_average_grade(self):
        pass

    def __repr__(self):
        return self.name


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}

    def set_id(self, id: int):
        self.student_id = id

    def get_id(self):
        return self.student_id

    def get_grades(self):
        return self.grades

    def get_average_grade(self):
        return sum(self.grades.values()) / len(self.grades)

    def add_grade(self, course, grade):
        self.grades[course] = grade

    def __repr__(self):
        return self.name


class School:
    def __init__(self):
        self.courses = []
        self.students = []

    def add_course(self, course):
        self.courses.append(course)

    def add_student(self, student):
        self.students.append(student)

    def add_student_grade(self, student: Student, course: Course, grade: int):
        student.add_grade(course.name, grade)

    def get_students(self):
        return self.students

    def get_courses(self) -> list[Course]:
        return self.courses

    def get_students_ordered_by_average_grade(self):
        return sorted(self.students, key=lambda s: s.get_average_grade(), reverse=True)


if __name__ == '__main__':
    # school has student who study
    students = []

    # it also has different courses/subjects
    courses = []

    # each student has name and unique id
    student1 = {'name': 'John Smith', 'id': '1'}
    student2 = {'name': 'Mary Lee', 'id': '2'}

    # let's add two students to university
    students.append(student1)
    students.append(student2)

    # let's see all the students:
    print(students)

    # let's add some courses
    course1 = "Math"
    course2 = "Physics"
    courses.append(course1)
    courses.append(course2)

    # each student should also have grades for courses
    # let's add a dict of grades to each student
    # the key is the subject, the value is the grade
    for student in students:
        # an empty list in the beginning
        student['grades'] = {}

    # student1 got 4 and 5
    student1['grades'][course1] = 4
    student1['grades'][course2] = 5

    # student2 got 5
    student2['grades'][course1] = 5

    # new student joins the university
    students.append({'name': 'Cocoo Turner', 'id': '3', 'grades': {}})

    # the new students gets some grades
    students[-1]['grades'][course1] = 3
    students[-1]['grades'][course2] = 5

    # print out students and their average grades, from the highest grade to lowest
    ordered_students = sorted(students, key=lambda s: sum(s['grades'].values()) / len(s['grades']), reverse=True)
    for student in ordered_students:
        print(student['name'], sum(student['grades'].values()) / len(student['grades']))

    # get average grades for each subject
    for course in courses:
        course_grades = []
        for student in students:
            for course_name, grade in student['grades'].items():
                if course_name == course:
                    course_grades.append(grade)
        print(course, sum(course_grades) / len(course_grades))
