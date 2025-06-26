std = {}
keys = ['id','city','name']

for i in range(len(keys)):
    value=input(f"Enter a value for {keys[i]} : ")
    std[keys[i]]=value
print(std)

