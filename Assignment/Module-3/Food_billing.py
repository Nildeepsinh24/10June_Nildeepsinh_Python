from datetime import datetime

name = input("Enter customer name: ")
mobile = input("Enter mobile number: ")
food = input("Enter food name: ")
price = float(input("Enter price of the item: "))
qty = int(input("Enter quantity: "))

total = price * qty
gst = total * 0.18
grand_total = total + gst

date = datetime.now().strftime("%d-%m-%Y")

with open("bill.txt", "w") as file:
    file.write("        Food Billing System\n")
    file.write("================================\n")
    file.write(f"Customer Name : {name}\n")
    file.write(f"Mobile Number : {mobile}\n")
    file.write(f"Date          : {date}\n")
    file.write("--------------------------------\n")
    file.write(f"Food Item : {food}\n")
    file.write(f"Price     : {price:.2f}\n")
    file.write(f"Quantity  : {qty}\n")
    file.write("--------------------------------\n")
    file.write(f"Total   : {total:.2f}\n")
    file.write(f"18% GST : {gst:.2f}\n")
    file.write("--------------------------------\n")
    file.write(f"Grand Total : {grand_total:.2f}\n")

print("✅ Bill saved to bill.txt")
