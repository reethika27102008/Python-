# studentdic= {"name":"Reethika",
#              "email":"reethika@gmail.com",
#              "mobile number":23456186567,
#              "isactive":True
#              }
# print(studentdic)

# print(type(studentdic))
# print(len(studentdic))
# print(studentdic["name"])
# print(studentdic.values())
# studentdic["total"]=573
# print(studentdic)
# studentdic.update({"mobile number":6383249502})
# print(studentdic)
# studentdic.pop("mobile number")
# print(studentdic)
studentdata = [
    {
        "name": "reethika",
        "email": "reethika@gmail.com",
        "marks": [91, 76, 87, 98, 90]
    },
    {
        "name": "ramya",
        "email": "ramya@gmail.com",
        "marks": [23, 65, 98, 90, 100]
    },
    {
        "name": "kavi",
        "email": "kavi@gmail.com",
        "marks": [56, 76, 1, 89, 78]
    }
]
for student in studentdata:
    total=0
    for mark in student["marks"]:
        total+=mark
        student["total"]=total

for i in range(len(studentdata)):
    for j in range(i+1,len(studentdata)):
        if studentdata[i]["total"]< studentdata[j]["total"]:
            studentdata[i],studentdata[j]=studentdata[j],studentdata[i]

for student in studentdata:
    mark=student["total"]
    if 300<mark<350:
        student["Remark"] ="Good"
    elif 350<mark<400:
        student["Remark"]="very good"
    elif 400<mark<450:
        student["Remark"]="Excellent"
    else:
        student["Remark"]="Better luck next time"

print(studentdata)