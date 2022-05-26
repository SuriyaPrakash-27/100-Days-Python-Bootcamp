student_heights = input("Input a list of student heights\n").split()

highest_height = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    if student_heights[n] > highest_height:
        highest_height = student_heights[n]

print(f"Highest height in the class is:{highest_height}")
