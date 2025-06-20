tech=["rajkot","ahmedabad","surat","navsari","baroda"]
print(tech.index("surat"))

for i in tech:
    print(i,"-", tech.index(i))

tech.append("limbdi")
print(tech)