# Average calculator
grades = []

x = True
while x:
    grade = float(input("Grade: "))
    if grade >= 0 and grade <= 10:
        grades.append(grade)
    elif grade == -1:
        x = False
    else:
        print("Grade must be from 0-10. Try again.")


def average(grade_list):
    sum = 0
    for grade in grade_list:
        sum += grade
    return sum / len(grade_list)


def minimum(grade_list):
    min = grade_list[0]
    for grade in grade_list:
        if grade < min:
            min = grade
    return min


def maximum(grade_list):
    max = grade_list[0]
    for grade in grade_list:
        if grade > max:
            max = grade
    return max


print(grades)
average_grade = average(grades)
min_grade = minimum(grades)
max_grade = maximum(grades)

print("Your average is " + str(average_grade))
print("Your minimum grade is " + str(min_grade))
print("Your maximum grade is " + str(max_grade))