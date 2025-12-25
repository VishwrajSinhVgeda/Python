class SchoolManagement:
    def __init__(self):
        # Stores students in the form:
        # { student_id: {"name": ..., "age": ..., "class": ..., "mobile": ...} }
        self.students = {}
        self.next_student_id = 1  # To generate unique student IDs

    def _generate_student_id(self):
        student_id = self.next_student_id
        self.next_student_id += 1
        return student_id

    def new_admission(self):
        print("\n--- New Admission ---")
        name = input("Enter student name: ").strip()

        # Age validation: must be integer between 5 and 18
        try:
            age = int(input("Enter age (5-18): "))
            if age < 5 or age > 18:
                print("Invalid age. Age must be between 5 and 18.")
                return
        except ValueError:
            print("Invalid age. Please enter a number.")
            return

        # Class validation: must be integer between 1 and 12
        try:
            std = int(input("Enter class (1-12): "))
            if std < 1 or std > 12:
                print("Invalid class. Class must be between 1 and 12.")
                return
        except ValueError:
            print("Invalid class. Please enter a number.")
            return

        # Mobile validation: 10 digits
        mobile = input("Enter guardian's mobile number (10 digits): ").strip()
        if not (mobile.isdigit() and len(mobile) == 10):
            print("Invalid mobile number. It must be 10 digits.")
            return

        # All good → create record
        student_id = self._generate_student_id()
        self.students[student_id] = {
            "name": name,
            "age": age,
            "class": std,
            "mobile": mobile
        }

        print(f"\nAdmission successful! Assigned Student ID: {student_id}")

    def view_student_details(self):
        print("\n--- View Student Details ---")
        try:
            student_id = int(input("Enter Student ID: "))
        except ValueError:
            print("Invalid ID. Please enter a number.")
            return

        student = self.students.get(student_id)
        if not student:
            print("No student found with this ID.")
            return

        print(f"\nDetails for Student ID {student_id}:")
        print(f"Name          : {student['name']}")
        print(f"Age           : {student['age']}")
        print(f"Class         : {student['class']}")
        print(f"Mobile Number : {student['mobile']}")

    def update_student_info(self):
        print("\n--- Update Student Info ---")
        try:
            student_id = int(input("Enter Student ID: "))
        except ValueError:
            print("Invalid ID. Please enter a number.")
            return

        student = self.students.get(student_id)
        if not student:
            print("No student found with this ID.")
            return

        print("\nWhat do you want to update?")
        print("1. Mobile Number")
        print("2. Class")
        choice = input("Enter choice (1 or 2): ").strip()

        if choice == "1":
            new_mobile = input("Enter new mobile number (10 digits): ").strip()
            if not (new_mobile.isdigit() and len(new_mobile) == 10):
                print("Invalid mobile number. It must be 10 digits.")
                return
            student["mobile"] = new_mobile
            print("Mobile number updated successfully.")
        elif choice == "2":
            try:
                new_class = int(input("Enter new class (1-12): "))
                if new_class < 1 or new_class > 12:
                    print("Invalid class. Class must be between 1 and 12.")
                    return
            except ValueError:
                print("Invalid class. Please enter a number.")
                return
            student["class"] = new_class
            print("Class updated successfully.")
        else:
            print("Invalid choice.")

    def remove_student_record(self):
        print("\n--- Remove Student Record ---")
        try:
            student_id = int(input("Enter Student ID: "))
        except ValueError:
            print("Invalid ID. Please enter a number.")
            return

        if student_id in self.students:
            del self.students[student_id]
            print("Student record removed successfully.")
        else:
            print("No student found with this ID.")

    def run(self):
        while True:
            print("\n===== School Management System =====")
            print("1. New Admission")
            print("2. View Student Details")
            print("3. Update Student Info")
            print("4. Remove Student Record")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ").strip()

            if choice == "1":
                self.new_admission()
            elif choice == "2":
                self.view_student_details()
            elif choice == "3":
                self.update_student_info()
            elif choice == "4":
                self.remove_student_record()
            elif choice == "5":
                print("Exiting system. Goodbye!")
                break
            else:
                print("Invalid choice. Please select from 1 to 5.")

school = SchoolManagement()
school.run()