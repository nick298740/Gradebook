from gradebook_definitions import Course
from gradebook_definitions import Student
from gradebook_definitions import Grade

class GradebookApplication:

    '''
    '''
    def startNewGradeBook(self):
        self.listOfCourses.clear()
      


    '''
    '''
    def addNewCourse(self):
        print('\nPlease enter the course name you would like to add:')
        courseName = input()
        self.listOfCourses.append(Course(courseName))

    
    '''
    '''
    def printAllCourses(self):
        for course in self.listOfCourses:
            print(course.courseName)

    
    '''
    '''
    def addNewStudent(self):
        print('\nPlease enter the students full name:')
        fullName = input()

        names = fullName.split(' ')
        firstName = names[0]
        lastName = names[1]

        self.listOfStudents.append(Student(firstName, lastName))

    
    '''
    '''
    def printAllStudents(self):
        for student in self.listOfStudents:
            print(student.fullName)

    
    '''
    '''
    def findStudent(self) -> Student:
        print('\nPlease enter students full name:')
        fullName = input()
        for student in self.listOfStudents:
            if fullName == student.fullName:
                return student
        return None


    '''
    '''
    def findCourse(self) -> Course:
        print('\nPlease enter the course name:')
        courseName = input()
        for course in self.listOfCourses:
            if courseName == course.courseName:
                return course
        return None

    
    '''
    '''
    def addStudentToCourse(self):
        student = self.findStudent()
        course = self.findCourse()

        if student != None or course != None:
            course.addStudentToCourse(student)

        else:
            print('Cannot add student to course:')
            if student == None:
                print('Could not find student')

            elif course == None:
                print('Could not find course')


    '''
    '''
    def addGradeToStudent(self):
        student = self.findStudent()
        course = self.findCourse()

        print('What was the grade?')
        gradeValue = input()

        if student != None or course != None:
            gradeObject = Grade(gradeValue, course, student)
            print('Grade added: ' + gradeObject.value \
                + ' to student ' + gradeObject.student.fullName \
                    + ' for course ' + gradeObject.course.courseName)

        else:
            print('Cannot add student to course:')
            if student == None:
                print('Could not find student')

            elif course == None:
                print('Could not find course')



    '''
    '''
    def printAllCourseGradesForStudent(self):
        student = self.findStudent()
        print('Student: ' + str(student.fullName))
        for grade in student.gradeList:
            print('For course ' + str(grade.course.courseName) + ', '\
            + 'Grade: ' + str(grade.value))

    '''
    '''
    def __init__(self):    
        self.listOfCourses = []
        self.listOfStudents = []
    


        while True:
            print('\n')
            print('What would you like to do? Press the corresponding number:')
            print('1 Start a new gradebook')
            print('2 Add a new course')
            print('3 Add a new student')
            print('4 Print all courses')
            print('5 Print all students')
            print('6 Find a student')
            print('7 Find a course')
            print('8 Add a student to a course')
            print('9 Print all students in a course')
            print('10 Add a grade to a student in selected course')
            print('11 Print all course grades for a student')
            print('-1 quit')
            print('\n')

            userInput = input()
            if userInput == '-1':
                break
            
            elif userInput == '1':
                self.startNewGradeBook()

            elif userInput == '2':
                self.addNewCourse()

            elif userInput == '3':
                self.addNewStudent()

            elif userInput == '4':
                self.printAllCourses()

            elif userInput == '5':
                self.printAllStudents()
            
            elif userInput == '6':
                student = self.findStudent()
                if student == None:
                    print('Student not found')
                else:
                    print(student.fullName)

            elif userInput == '7':
                course = self.findCourse()
                if course == None:
                    print('Course not found')
                else:
                    print(course.courseName)

            elif userInput == '8':
                self.addStudentToCourse()

            elif userInput == '9':
                course = self.findCourse()
                course.printAllStudentsInCourse()

            elif userInput == '10':
                self.addGradeToStudent()
            
            elif userInput == '11':
                self.printAllCourseGradesForStudent()
                

