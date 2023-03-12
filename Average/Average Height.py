# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
num_of_students = 0
sum = 0
total = ""
for i in student_heights:
  sum += i
  num_of_students += 1
  total = round(sum / num_of_students)
print(total)

