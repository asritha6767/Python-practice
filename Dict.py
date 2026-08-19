
# Day 6: Dictionaries
student = {
    "name": "Asritha",
    "age": 20,
    "course": "Python"
}

print("Name:", student["name"])
print("Course:", student["course"])

for key, value in student.items():
    print(key, ":", value)