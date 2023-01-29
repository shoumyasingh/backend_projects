import csv


class Data:

    def add__student(self, student_id, first_name, last_name) -> None:
        with open('Student.csv', 'a') as file:
            file.write("%s,%s,%s\n" % (student_id, first_name, last_name))

    def read__student(self, student_id):
        student_details = {}

        with open('Student.csv', newline="") as file:
            for line in file.readlines():
                line_list = line.split(',')
                if line_list[0].strip() == str(student_id):
                    student_details[student_id] = [line_list[1], line_list[2]]
            if not student_details:
                print("Enter a valid student id.")
        return student_details

    def write__policy(self, a_num, t_num, f_num, a_wt, t_wt, f_wt):
        with open('Policy.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['Assignments Number', a_num])
            writer.writerow(['Tests Number', t_num])
            writer.writerow(['Final Exam Number', f_num])

            writer.writerow(['Assignment Weight', a_wt])
            writer.writerow(['Test Weight', t_wt])
            writer.writerow(['Final Exam Weight', f_wt])

    def read__policy(self):
        policy = {}
        with open('Policy.csv', newline="\n") as file:
            reader = csv.reader(file)
            for row in reader:
                policy[row[0]] = row[1]
        return policy