marks = int(input("Enter the marks: "))
def grade_check(grade):
    if grade >= 90:
        gr = "A"
    elif grade >= 80:
        gr = "B"
    elif grade >= 70:
        gr = "C"
    elif grade >= 60:
        gr = "D"
    else:
        gr = "F"
    return {"your input": grade, "result": gr}


print(grade_check(marks))