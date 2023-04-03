class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lc(self, lectore, course, grade):
        if isinstance(lectore, Lecturer) and course in lectore.courses_attached and course in self.courses_in_progress:
            if course in lectore.grades:
                lectore.grades[course] += [grade]
            else:
                lectore.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def average(self):
        sum_a = sum(self.grades.values(), [])
        len_a = len(sum_a)
        count = 0
        for i in sum_a:
            count += i
        itogo = count / len_a
        return itogo

    def __str__(self):
         res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
         return res
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Net takogo studenta')
            return
        return self.average() < other.average() 

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
       
    def average(self):
        sum_a = sum(self.grades.values(), [])
        len_a = len(sum_a)
        count = 0
        for i in sum_a:
            count += i
        itogo = count / len_a
        return itogo

    def __str__(self):
         res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average()}'
         return res
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Net lektora')
            return
        return self.average() < other.average()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
         res = f'Имя: {self.name}\nФамилия: {self.surname}'
         return res

def avg_cours_stud(lst, key):
    sum_av = []
    count_2 = 0
    for i in lst:
        sum_av += i[key]
    for g in sum_av:
        count_2 += g
    naconecto_3 = count_2 / len(sum_av)
    return naconecto_3    

student_1 = Student('Leha', 'Naval', 'm.')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['VB']
student_1.finished_courses += ['C++']

student_2 = Student('Sofia', 'Sopega', 'w.')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['C++']
student_2.finished_courses += ['VB']

reviewer_1 = Reviewer('Sergei', 'Darnitskij')
reviewer_1.courses_attached += ['VB']
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Drus', 'Arbus')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['C++']

lecturer_1 = Lecturer('Sanja', 'Sertolovskij')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['VB']

lecturer_2 = Lecturer('Ivan', 'Icon')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['C++']

reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 5)
reviewer_1.rate_hw(student_1, 'VB', 9)

reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 3)
reviewer_2.rate_hw(student_2, 'C++', 10)

student_1.rate_lc(lecturer_1, 'Python', 9)
student_1.rate_lc(lecturer_1, 'VB', 9)
student_1.rate_lc(lecturer_1, 'Python', 8)

student_2.rate_lc(lecturer_2, 'Python', 8)
student_2.rate_lc(lecturer_2, 'VB', 8)
student_2.rate_lc(lecturer_2, 'Python', 9)

print(student_1, student_2, sep='\n')

print(reviewer_1, reviewer_2, sep='\n')

print(lecturer_1, lecturer_2, sep='\n')

print(student_1 > student_2)

print(lecturer_1 > lecturer_2)

print(avg_cours_stud([student_1.grades, student_2.grades], 'Python'))

print(avg_cours_stud([lecturer_1.grades, lecturer_2.grades], 'Python'))