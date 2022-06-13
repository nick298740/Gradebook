

class Course:

    '''
    '''
    def addStudentToCourse(self, student):
        self.studentsInCourse.append(student)


    '''
    '''
    def printAllStudentsInCourse(self):
        for i in range(len(self.studentsInCourse)):
            print(self.studentsInCourse[i].fullName)


    '''
    Constructor for the object Course 
    ''' 
    def __init__(self, p_courseName):
        self.courseName = p_courseName
        self.studentsInCourse = []


class Student:

    
    '''
    Constructor for the object Student 
    '''
    def __init__(self, p_firstName, p_lastName):
        self.firstName = p_firstName
        self.lastName = p_lastName
        self.fullName = self.firstName + ' ' + self.lastName
        self.gradeList = []
    
    
    '''
    '''
    def getGradeOfCourse(self, p_course):
        for grade in self.gradeList:
            if grade.course == p_course:
                return grade
        return None




class Grade:


    '''
    Constructor for the object Grade 
    '''
    def __init__(self, p_gradeValue, p_course, p_student):
        self.value = p_gradeValue
        self.course = p_course
        self.student = p_student

        self.addGradeToStudent(self.student)


    '''
    '''
    def addGradeToStudent(self, p_student):
        p_student.gradeList.append(self)

