tup = int(input("Enter number of Student Names to be inserted: "))
student = set()
for i in range(tup):
    std = input("Student Name: ")
    student.add(std)
print(student)