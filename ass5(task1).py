dictstd = {"roy": 9, "Prince": 8, "john": 4, "ansh": 7}

sname= input("Enter the student's name: ")

if sname in dictstd:
    print(sname+"'s marks:" ,dictstd[sname])
else:
    print("student details not found.")