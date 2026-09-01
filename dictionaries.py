student = {"name": "Mary",
           "age": 23,
           "university": "USIU"}
print(student["university"])

student = {"name": "John",
           "age": 20,
           "university": "Strathmore"}
student["course"] = "Literature"
student["course"] = "Political Science"
del student["age"]
print(student)