'''
2. Student Grades
Create a dictionary where the keys are student names and the values are their grades. Allow the user to:
Add a new student and grade.
Update an existing student's grade.
Print all student grades.
Use a dictionary and basic operations with if / else.

'''

student_grades = {}

while True:
	print("\n1. Add a student")
	print("2. Update a student's grade")
	print("3. Print all student grades")
	print("4. Exit")
	choice = input("Choose an option: ")

	if choice == "1":
		name = input("Student name: ")
		if name in student_grades:
			print("That student already exists.")
		else:
			grade = input("Grade: ")
			student_grades[name] = grade
			print("Student added.")
	elif choice == "2":
		name = input("Student name: ")
		if name in student_grades:
			student_grades[name] = input("New grade: ")
			print("Grade updated.")
		else:
			print("Student not found.")
	elif choice == "3":
		if student_grades:
			for name, grade in student_grades.items():
				print(f"{name}: {grade}")
		else:
			print("No student grades to display.")
	elif choice == "4":
		break
	else:
		print("Invalid option. Please choose 1, 2, 3, or 4.")
