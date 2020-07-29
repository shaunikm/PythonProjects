def get_student_names(students):
    z = []
    k = 1
    for i in students:
        z.append(students[i])
        k += 1
    return sorted(z)


print(get_student_names({
    "Student 1": "Steve",
    "Student 2": "Becky",
    "Student 3": "John"
}))