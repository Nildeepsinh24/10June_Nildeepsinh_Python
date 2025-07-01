x=open("num.txt","a")
for i in range(1,101):
    print(i)
    x.write(f"{str(i)}\n")