class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка' 
        
    def average_rating (self):
        count = 0
        count2 = 0
        for course in self.grades:
            for grade in self.grades[course]:
                count += grade
                count2 +=1
        return (count/count2)
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_rating()}\nКурсы в процессе изучения: {','.join(self.courses_in_progress)}\nЗавершенные курсы: {','.join(self.finished_courses)}"

        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
   
    
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def average_rating (self):
        count = 0
        count2 = 0
        for course in self.grades:
            for grade in self.grades[course]:
                count += grade
                count2 +=1
        return (count/count2)
    

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating()}"
    
    
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка' 
        
    def __str__(self) -> str:
        return f"Имя: {self.name}\nФамилия: {self.surname}"
def comparison_lecurer(lecture1,lecture2):
    if lecture1.average_rating() > lecture2.average_rating():
        print (f'Рейтинг лектора {lecture1.name} {lecture1.surname} выше чем рейтинг лектора {lecture2.name} {lecture2.surname}')
    elif lecture1.average_rating() < lecture2.average_rating():
        print (f'Рейтинг лектора {lecture1.name} {lecture1.surname} ниже чем рейтинг лектора {lecture2.name} {lecture2.surname}')
    else:print ("Оба лектора молодцы")

def comparison_students(student1,student2):
    if student1.average_rating() > student2.average_rating():
        print (f'Оценки студента {student1.name} {student1.surname} выше чем оценки студента {student2.name} {student2.surname}')
    elif student1.average_rating() < student2.average_rating():
        print (f'Оценки студента {student1.name} {student1.surname} ниже чем оценки студента {student2.name} {student2.surname}')
    else:print ("У этих студентов одинаковая успеваемость")
def average_homework_score(student_list,course):
    count1 = 0
    count3 = 0
    for student in student_list:
        if course in student.grades:
            for grade in student.grades[course]:
                count1 += grade
                count3 += 1
    print(f"Средний балл за домашнее задание на курсе {course} = {count1/count3}") 

def average_lectures_score(lectures_list,course):
    count1 = 0
    count3 = 0
    for lecturer in lectures_list:
        if course in lecturer.grades:
            for grade in lecturer.grades[course]:
                count1 += grade
                count3 += 1
    print(f"Средняя оценка за лекции на курсе {course} = {count1/count3}")         

reviewer1 = Reviewer("Алёна","Апина")
reviewer2 = Reviewer("Олег","Газманов")
lecturer1 = Lecturer('Сергей',"Галанин")
lecturer2 = Lecturer("Дмитрий","Дибров")
student1 = Student("Михаил","Мухин","male")
student2 = Student("Сяо","Ли","female")

student1.courses_in_progress += ['Python',"Git"]
student1.finished_courses += ["Введение в программирование"]
student2.courses_in_progress += ['Python',"Git"]
student2.finished_courses += ["Введение в программирование"]
reviewer1.courses_attached += ['Git']
reviewer2.courses_attached += ['Python'] 
lecturer1.courses_attached += ['Python']
lecturer2.courses_attached += ['Git'] 
reviewer1.rate_hw(student1, 'Git', 10)
reviewer1.rate_hw(student2, 'Git', 9)
reviewer1.rate_hw(student1, 'Git', 7)
reviewer1.rate_hw(student2, 'Git', 8)
reviewer2.rate_hw(student1, 'Python', 8)
reviewer2.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student1, 'Python', 6)
reviewer2.rate_hw(student2, 'Python', 7)
student1.rate_hw(lecturer1, 'Python', 9)
student2.rate_hw(lecturer1, 'Python', 10)
student1.rate_hw(lecturer1, 'Python', 8)
student2.rate_hw(lecturer1, 'Python', 7)
student1.rate_hw(lecturer2, 'Git', 6)
student2.rate_hw(lecturer2, 'Git', 7)
student1.rate_hw(lecturer2, 'Git', 10)
student2.rate_hw(lecturer2, 'Git', 10)

student_list = [student1,student2]
lectures_list = [lecturer1,lecturer2]


print (student1)
print (student2)
comparison_students(student1,student2)
average_homework_score(student_list,"Python")
average_homework_score(student_list,"Git")
print (lecturer1)
print (lecturer2)
average_lectures_score(lectures_list,"Git")
average_lectures_score(lectures_list,"Python")
comparison_lecurer(lecturer1,lecturer2)   
print (reviewer1)
print (reviewer2)
