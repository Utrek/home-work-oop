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
        for course in self.grades:
            for grade in self.grades[course]:
                count += grade
        return count / len(self.grades[course])
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating()}\nКурсы в процессе изучения: {','.join(self.courses_in_progress)}\nЗавершенные курсы: {','.join(self.finished_courses)}"

        
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
        for course in self.grades:
            for grade in self.grades[course]:
                count += grade
        return count / len(self.grades[course])
    

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

    
horn = Reviewer("Jon","Bow")

pop = Lecturer("Jim", "Bim")
pok = Lecturer("Jon","Snow")
pol = Student ("Kin","Cen","Men")
pot = Student ("Миша","Мухин","Fly")
pol.courses_in_progress += ['Python',"Git"]
pol.finished_courses += ["Введение в программирование"] 
pot.courses_in_progress += ['Python',"Git"]
pot.finished_courses += ["Введение в программирование"] 
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.rate_hw(pot, 'Python', 8)
cool_mentor.rate_hw(pot, 'Python', 7)
cool_mentor.rate_hw(pot, 'Python', 6)
cool_mentor.rate_hw(pol, 'Python', 10)
cool_mentor.rate_hw(pol, 'Python', 7)
cool_mentor.rate_hw(pol, 'Python', 3)
pop.courses_attached += ['Python']
pok.courses_attached += ["Python"]
pol.rate_hw(pop, 'Python', 8)
pol.rate_hw(pop, 'Python', 7)
pol.rate_hw(pop, 'Python', 3)
pol.rate_hw(pok, 'Python', 10)
pol.rate_hw(pok, 'Python', 7)
pol.rate_hw(pok, 'Python', 5)
comparison_lecurer(pop,pok)
comparison_students(pol,pot)
print(horn)
print(pop)
print(pok)
print(pol)
print(pot)