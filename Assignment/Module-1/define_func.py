"""def myfunc():
    print("This Is USER DEFINE FUNCTION")

def getsum(a,b):
    print("SUM: ",a+b)

myfunc()
getsum(5,5)"""

def getdata(id,name,city):
    print("Id:",id)
    print("Name:",name)
    print("City:",city)
#getdata(101,"ABC","Rajkot")
stid = int(input("Enter Id:"))
stname = input("Enter Name: ")
stcity = input("Enter City: ")

getdata(stid,stname,stcity)