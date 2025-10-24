from modules.student_manager import StudentManager

def main():
    manager = StudentManager()

    while True:
        print("\n1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Remove Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter Student ID: ")
            first_name = input("Enter First Name: ")
            surname = input("Enter Surname: ")
            manager.add_student(student_id, first_name, surname)

        elif choice == "2":
            manager.display_students()

        elif choice == "3":
            student_id = input("Enter ID to search: ")
            manager.search_student(student_id)

        elif choice == "4":
            student_id = input("Enter ID to remove: ")
            manager.remove_student(student_id)

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
