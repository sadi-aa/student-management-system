from manager import StudentManager

sm = StudentManager()

while True:
    print("\n1. Add Student\n2. View Students\n3. Update Student\n4. Delete Student\n5. Exit")
    choice = input("Choose option: ")
    if choice == '1':
        n = input("Name: ")
        a = int(input("Age: "))
        i = input("ID: ")
        sm.create_student(n, a, i)
    elif choice == '2':
        sm.view_students()
    elif choice == '3':
        i = input("Enter ID to update: ")
        n = input("New Name: ")
        a = int(input("New Age: "))
        sm.update_student(i, n, a)
    elif choice == '4':
        i = input("Enter ID to delete: ")
        sm.delete_student(i)
    elif choice == '5':
        break
