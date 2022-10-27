class student:
    def __init__(self,name,matric):
        self.name = name
        self.matric = matric
        self.courses = []
        self.gpa = 0
    def add_course(self,course,grade,unit):
        return self.courses.append( { 'title': course, 'unit': unit, 'grade': grade } )
    def calculate_gpa(self):
        unitSum = 0
        score = 0
        grades = ['A', 'B', 'C', 'D', 'E', 'F']
        for course in self.courses:
            unitSum += course['unit']
            score += course['unit'] * (grades.index(course['grade']))
        self.gpa = score/unitSum
    def rank_student_by_gpa(self):
        if self.gpa >= 4.5:
            return('{self.name} is a first class student')
        elif self.gpa >= 3.5 and self.gpa < 4.5:
            return('{self.name} is a second class upper student')
        elif self.gpa >= 2.4 and self.gpa < 3.5:
            return('{self.name} is a second class lower student')
        else:
            return('{self.name} is a third class student')
student1 = student('SALAU MUHAMMED', '190407083')
student1.add_course('SSG215', 'A', '3')
student1.add_course('MEG212', 'A', '2')
student1.add_course('MEG211', 'A', '2')
student1.add_course('CEG211', 'B', '3')
student1.add_course('GEG219', 'A', '3')
student1.add_course('EEG213', 'A', '2')

student1.calculate_gpa()
print(student1.rank_student_by_gpa())
