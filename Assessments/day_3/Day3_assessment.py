# Class: Student
class Student:
    #constructor
    def __init__(self, sid, name, course, average_marks):
        self.sid = sid
        self.name = name
        self.course = course
        self.average_marks= average_marks
    #using __str__ displays all the student data
    def __str__(self):
        return f" Student ID: {self.sid}\n Name: {self.name}\n Course: {self.course}\n Average Marks: {self.average_marks}\n"

# Class: StudentManagement
class StudentManagement:
    #constructor
    def __init__(self):
        self.students = {}  # sid as key
    #adding of student
    def add_student(self, student):
        self.students[student.sid] = student
        print("Student added successfully!")
    #viewing the list of student entries
    def view_all(self):
        if not self.students:
            print("No students available.")
        for student in self.students.values():
            print(student)
    # TO update the student table
    def update_student(self, sid, name, course, average_marks):
        if sid in self.students:
            if name:
                self.students[sid]["name"] = name
            if course:
                self.students[sid]["course"] = course
            if average_marks:
                self.students[sid]["average_marks"] = average_marks
            print("Student updated.")
        else:
            print("Student not found.")

    # To Delete the student record
    def delete_student(self, sid):
        removed = self.students.pop(sid)
        if removed:
            print("Student deleted.")
        else:
            print("Student not found.")

# Main Program
def main():
    data = StudentManagement()
    #main operation
    try:
        while True:
            print("\n--- Student Management System ---")
            print("1. Add Student")
            print("2. View All Students")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Exit")

            choice = int(input("Enter choice (1-5):"))

            if choice == 1:
                id = int(input("Enter Student ID: "))
                name = input("Enter Name: ")
                course = input("Enter Course: ")
                average = float(input("Enter Average marks"))
                student = Student(id, name, course,average)
                data.add_student(student)

            elif choice == 2:
                data.view_all()

            elif choice == 3:
                id = int(input("Enter Student id to update: "))
                name = input("Enter new name")
                course = input("Enter new course")
                average= float(input("enter the average marks"))
                data.update_student(id, name, course, average)

            elif choice == 4:
                id = int(input("Enter Enter student ID to delete: "))
                data.delete_student(id)
            elif choice == 5:
                print("*********Exiting**********")
                break
            else:
                print("*******************Invalid choice********************")
    except ValueError:
        print("enter Numeric values only")
# To Run the App
if __name__ == "__main__":
    main()