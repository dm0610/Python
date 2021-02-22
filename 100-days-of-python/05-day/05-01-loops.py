student_heights = input("Input a list of a student Heigts ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

print(len(student_heights))



total_height = sum(student_heights)
number_of_students = len(student_heights)
average_height = round(total_height / number_of_students)
print("average_height:", average_height)


number_of_students = 0
for student in student_heights:
    number_of_students += 1

average_height = round(total_height / number_of_students)
print(average_height)

