s1=int(input("Enter The Marks For Subject 1:"))
s2=int(input("Enter The Marks For Subject 2:"))
s3=int(input("Enter The Marks For Subject 3:"))
s4=int(input("Enter The Marks For Subject 4:"))

total = s1+s2+s3+s4
print("Total is:",total)

pr = total/400*100
print("Percentage is:",pr)

if pr > 70:
    print("Distinction")
elif pr > 60:
    print("First Class")
elif pr > 50:
    print("Second Class")
else:
    print("FAIL")