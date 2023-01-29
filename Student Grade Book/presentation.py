from business import Student, Policy, Score


class GradeBook:

    def __init__(self):
        self.__policy = Policy()
        self.__score = Score()
        self.__student = Student("", "", "")
        self.__filename = 'Grades.dat.csv'

    def showTitle(self):
        print("The GradeBook program for the student\n")

    def showMenu(self):
        print("COMMAND MENU for Grade Management")
        print("S - Set up for new semester")
        print("A - Add a student")
        print("P - Record programming assignment score")
        print("T - Record test score")
        print("F - Record Final exam score")
        print("C - Change grade")
        print("G - Calculate final score")
        print("O - Output the grade data")
        print("Q - Quit")
        print()

    def setSemester(self):
        self.__policy.set_semester()
        self.__policy.write_policy()
        self.__policy.read_policy()

    def readStudent(self, student_id):
        return self.__student.read_student(student_id)

    def addStudent(self):
        student_id = input("Enter the Student Id: ")
        first_name = input("Enter the first name: ")
        last_name = input("Enter the last name: ")
        self.__student.add_student(student_id, first_name, last_name)
        print(student_id + " is added.\n")

    def recordAssgntScore(self):
        student_id = input("Enter the Id of Student: ")
        dict_student = self.__student.read_student(student_id)
        self.print_student(dict_student, student_id)
        assgnt_number = int(input("Enter assignment number: "))
        policy = self.__policy.read_policy()
        policy_assgnt_number = int(policy["Assignments Number"])

        if assgnt_number < 0 or assgnt_number > policy_assgnt_number:
            print("Entered assignment is Invalid, Please return valid one: ")
            assgnt_number = input("Enter the correct assignment number: ")

        assgnt_score = int(input("Enter assignment related to student with ID " + student_id + ":"))
        self.__score.write_score(student_id, "Assignment", assgnt_number, assgnt_score)
        print("Assignment record saved in a file")

    def recordTestScore(self):
        student_id = input("Enter the Student Id: ")
        dict_student = self.__student.read_student(student_id)
        self.print_student(dict_student, student_id)
        test_number = int(input("Enter the test number: "))
        policy = self.__policy.read_policy()
        policy_test_number = int(policy["Tests Number"])

        if test_number < 0 or test_number > policy_test_number:
            print("Invalid Test number, Please provide the valid one: ")
            test_number = input("Enter the test number: ")

        test_score = int(input("Enter test score for student with ID " + student_id + ":"))
        self.__score.write_score(student_id, "Test", test_number, test_score)
        print("Test Score record updated in the file")

    def recordFinalExamScore(self):
        student_id = input("Enter the Student Id: ")
        dict_student = self.__student.read_student(student_id)
        self.print_student(dict_student, student_id)
        final_exam_number = int(input("Enter about final exam number: "))
        policy = self.__policy.read_policy()
        policy_final_exam_number = int(policy["Final Exam Number"])

        if final_exam_number < 0 or final_exam_number > policy_final_exam_number:
            print("Invalid Final exam number, Please return valid one: ")
            final_exam_number = input("Enter the final exam number: ")

        final_exam_score = int(input("Enter final exam score for student for given ID " + student_id + ":"))
        self.__score.write_score(student_id, "FinalExam", final_exam_number, final_exam_score)
        print("Final exam score updated in the file")

    def changeScore(self):
        student_id = input("Enter the Student Id for update the score: ")
        type_of_score = input("Enter the type of Score:  T(Test) or F(Final Exam) or A(Assignment)")
        number = input("Enter which A(Assignment) or F(Final Exam) or T(Test) or number: ")
        change_score = input("Enter the new score for student with ID " + student_id + ":")

        self.__score.record_score(change_score, number, student_id, type_of_score)

    def print_student(self, dict_student, student_id):
        for k, v in dict_student.items():
            if student_id == k:
                print("Student Name is:", end=" ")
                for name in v:
                    print(name, end=" ")

    def get_final_score(self):

        self.__score.calculate_final_score()

    def output_grade_book(self):

        self.__score.calculate_final_score()



def main():
    app = GradeBook()

    app.showTitle()
    app.showMenu()

    while True:
        command = input("Command: ")
        command = command.lower()
        if command == "s":
            app.setSemester()
        elif command == "a":
            app.addStudent()
        elif command == "p":
            app.recordAssgntScore()
        elif command == "t":
            app.recordTestScore()
        elif command == "f":
            app.recordFinalExamScore()
        elif command == "c":
            app.changeScore()
        elif command == "g":
            app.get_final_score()
        elif command == "o":
            app.output_grade_book()
        elif command == "q":
            print('Bye!')
            break
        else:
            print("Not a valid command for the Grade System. Please try again.\n")


if __name__ == "__main__":
    main()
