import re

class Student:
    def __init__(self, name, matric, grades, units):
        self._name = name
        self._matric = matric
        self._grades = grades
        self._units = units
    def name(self):
        return self._name
    
    def matric(self):
        return self._matric
    
    def __rep__(self):
        return self._grades
    
        # return grades

    def units(self):
        return self._units
    


    def gpa(self):
        sumOfGradePoints = 0
        sumOfQualityPoints = 0
        quality_point = 0
        grade_point = 0
        for num in self._grades:
            if num >= 70:
                grade_point = 5.0
                quality_point += self._units[self._grades.index(num)] * grade_point
            elif 60 <= num <= 69:
                grade_point = 4.0
                quality_point += self._units[self._grades.index(num)] * grade_point
            elif 50 <= num <= 59:
                grade_point = 3.0
                quality_point +=  self._units[self._grades.index(num)] * grade_point
            elif 45 <= num <= 49:
                grade_point = 2.0
                quality_point +=  self._units[self._grades.index(num)] * grade_point
            elif 40 <= num <= 44:
                grade_point = 1.0
                quality_point +=  self._units[self._grades.index(num)] * grade_point
            else:
                grade_point = 0.0
                quality_point +=  self._units[self._grades.index(num)] * grade_point

        
        total = quality_point / sum(self._units)
        if 4.50 <= total <= 5.0:
            return "Your GPA is {:.2f} You are in first class".format(total)
        elif 3.5 <= total <= 4.49:
            return "Your GPA is {:.2f} You are in second class upper".format(total)
        elif 2.5 <= total <= 3.49:
            return "Your GPA is {:.2f} You are in second class lower".format(total)
        elif 2.0 <= total <= 2.49:
            return "Your GPA is {:.2f} You are in third class".format(total)
        elif 1.5 <= total <= 1.99:
            return "Your GPA is {:.2f} You are in pass".format(total)
        else:
            return "Your GPA is {:.2f} You are not in good standing".format(total)
        
    def __str__(self):
        return self.gpa()

    def get_gp(self):
        return float("".join(re.findall('\d\.\d\d', self.gpa())))
    


gradesForStudent_1 = [73, 61, 62, 56, 61, 71, 78, 58, 73, 78, 90, 45, 90, 73, 70]

gradesForStudent_2 = [53, 61, 62, 60, 45, 71, 78, 58, 73, 53, 90, 55, 70, 73, 70]

gradesForStudent_3 = [43, 61, 52, 60, 61, 61, 78, 58, 53, 63, 72, 45, 90, 53, 70]
units = [2, 3, 3, 2, 2, 2, 1, 3, 2, 3, 4, 1, 2, 3, 4]

studentOne = Student("kemi", "100405003", gradesForStudent_1, units)
studentTwo = Student("Seun", "100405025", gradesForStudent_2, units)
studentThree = Student("chioma", "100405067", gradesForStudent_3, units)

print(studentOne.gpa())
print(studentTwo.gpa())
print(studentThree.gpa())

print("\n")
listOfGps = [studentOne.get_gp(), studentTwo.get_gp(), studentThree.get_gp()]

print(listOfGps)

        

