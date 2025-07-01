with open("temp.txt", "a") as x:
    students = int(input("Enter Number Of Students: "))

    for i in range(students):
        print(f"\nEnter Details: {i+1}")
        student_id = input("Enter an ID: ")
        name = input("Enter a name: ")
        city = input("Enter a city: ")

        x.write(f"\nID: {student_id}")
        x.write(f"\nNAME: {name}")
        x.write(f"\nCITY: {city}")
        x.write("\n------------------------------------------\n")