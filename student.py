my_file=open("student.txt","w")

print(my_file.write(input("enter the student id :\n")))
print(my_file.write(" "))
print(my_file.write(input("enter the student name :\n")))
print(my_file.write(" "))
print(my_file.write(input("enter the student course :\n")))
print(my_file.write("\n"))

my_file=open("student.txt","r")
print(my_file.read())

