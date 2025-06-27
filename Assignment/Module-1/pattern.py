#for i in range(1,6):
#    for j in range(i):
#        print("*",end="")
#    print(" ")

#for i in range(1, 6):           #1 22 333 4444 55555
#    for j in range(i):
#        print(i, end="")
#    print()

#for i in range(1,6):           #1 12 123 1234 12345
#    for j in range(i):
#        print(j+1, end="")
#    print()

for i in range(5,0,-1):     #reverse *
    for j in range(i):
        print("* ",end="")
    print(" ")

for i in range(1,6):           #a bb ccc dddd eeeee
    for j in range(i):
        print(chr(96+i), end=" ")
    print(" ")

