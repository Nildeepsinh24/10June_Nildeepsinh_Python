class Marks:
    def getmark(self):
        self.s1 = int(input("Enter Subject 1 Mark: "))
        self.s2 = int(input("Enter Subject 2 Mark: "))
        self.s3 = int(input("Enter Subject 3 Mark: "))
        self.s4 = int(input("Enter Subject 4 Mark: "))
        print("-----------------------------------------")

class Result(Marks):
    def printresult(self):
        print("\n---MARKS OBTAINED ARE---")
        print("Subject 1 Marks Are:", self.s1)
        print("Subject 2 Marks Are:", self.s2)
        print("Subject 3 Marks Are:", self.s3)
        print("Subject 4 Marks Are:", self.s4)
        total = self.s1 + self.s2 + self.s3 + self.s4
        per = total / 4
        print("\nTotal Marks:", total)
        print("\nPercentage:", per)

r = Result()
r.getmark()
r.printresult()
