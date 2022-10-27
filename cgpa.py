class Student:

    def __init__(self, name, matric, grades):
        self._matric = matric
        self._name = name
        self._grades = grades
        self.courses_point = [3, 3, 2, 3, 2, 3, 1, 4, 4, 5, 1, 2, 2, 4, 1]
    
    def getName(self):
        return self._name

    def getMatric(self):
        return self._matric

    def getGrades(self):
        return self._grades

    def calculate_gpa(self):
        total = 0
        for i in range(len(self._grades)):
            grade_point = self._grade_value(self._grades[i])
            total += (grade_point * self.courses_point[i])
        return total / sum(self.courses_point)

    def _grade_value(self, value):
        point = 0
        if value >= 70:
            point = 5
        elif value >= 60:
            point = 4
        elif value >= 50:
            point = 3
        elif value >= 40:
            point = 2
        elif value >= 30:
            point = 1

        return point
            


# Tests

g1 = [82, 92, 93, 94, 95, 96, 77, 88, 99, 90, 96, 88, 94, 96, 90]
g2 = [33, 28, 82, 99, 8, 76, 91, 20, 65, 82, 35, 76, 54, 100, 10]
g3 = [17, 27, 13, 5, 17, 46, 12, 18, 45, 10, 54, 29, 43, 29, 10]
g4 = [69, 32, 93, 49, 45, 63, 57, 48, 79, 42, 86, 11, 22, 56, 20]

n1="Levi"
n2="Mikasa"
n3="Erwin"
n4="Kenny"

m1="12345QC"
m2="98989BG"
m3="22445CF"
m4="87654OP"

student_list = [Student(n1, m1, g1), Student(n2, m2, g2), Student(n3, m3, g3), Student(n4, m4, g4)]

# QUESTION 1 ------ CGPA of each student
print('------------------ GPA LIST OF ALL STUDENTS ------------------------------')
for student in student_list:
    print(f'{student.getName()} -- {student.calculate_gpa()}')

# QUESTION 2 -------- Rank each student
print('------------------- Rank of all Students ------------------------------------')
std_avg_dict = {f'{student.calculate_gpa()}': f'{student.getName()}' for student in student_list}

rank = 1
# Assuming all GPAs are unique.
for student_rank in sorted(std_avg_dict.keys(), reverse=True):
    print(f'Rank: #{rank} -------- {std_avg_dict[student_rank]}')
    rank += 1


# QUESTION 3 ----------------- Mark student automatically if bad standing --------------------
print('------------------- Mark bad students????? ------------------------------------')
for student_rank in sorted(std_avg_dict.keys(), reverse=True):
    # If student has an F, bad standing...
    if float(student_rank) < 1:
        print(f'Try better: {std_avg_dict[student_rank]} ---- {student_rank} is really poor!!!')

# QUESTION 4 ----------------- List of GPA --------------------
print('------------------- List of GPA ------------------------------------')
print([student.calculate_gpa() for student in student_list])


