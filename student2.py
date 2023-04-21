students = int(input("Please enter the amount of students registered."))
id_number = ""

for a in range (0, students):
    id_number = (int(input("Please enter student ID numbers.")))
    id_number = id_number + 1
    with open('student.txt', 'w') as file:
        file.write("Student ID numbers: \n" + str(id_number))

print ("Thank you, ID numbers saved to txt file reg_form")