student_heights = input("Input a list of student heights\n").split()

sum = 0
count = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    sum += student_heights[n]
    count += 1

average = round(sum/count)

print(average)



