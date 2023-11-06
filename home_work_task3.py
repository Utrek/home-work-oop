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
        return f"Имя: {self.name} Фамилия: {self.surname} Средняя оценка за лекции: {self.average_rating()} Курсы в процессе изучения: {self.courses_in_progress} Завершенные курсы: {self.courses_in_progress}"

        
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
        return f"Имя: {self.name} Фамилия: {self.surname} Средняя оценка за лекции: {self.average_rating()}"
    
    
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
        return f"Имя: {self.name} Фамилия: {self.surname}"
    
    
horn = Reviewer("Jon","Bow")

pop = Lecturer("Jim", "Bim")

pol = Student ("Kin","Cen","Men")


pol.courses_in_progress += ['Python']
 
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(pol, 'Python', 10)
cool_mentor.rate_hw(pol, 'Python', 7)
cool_mentor.rate_hw(pol, 'Python', 3)
pop.courses_attached += ['Python']
pol.rate_hw(pop, 'Python', 8)
pol.rate_hw(pop, 'Python', 7)
pol.rate_hw(pop, 'Python', 3)

