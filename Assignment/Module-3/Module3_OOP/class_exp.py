class student:
    stid=12
    stnm="ABC"

    def myfunc(self):
        print("This is member function of Student Class.")

st = student()
print("ID: ",st.stid)
print("NAME: ",st.stnm)

st.myfunc()
