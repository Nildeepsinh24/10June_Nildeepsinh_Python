x = open("temp.txt","w")
#x.write("Hello Python")

id = input("Enter an ID:")
name = input("Enter an name:")
city = input("Enter an city:")

x.write(f"ID: {id}")
x.write(f"\nNAME: {name}")
x.write(f"\nCity: {city}")