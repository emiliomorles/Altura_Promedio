student_heights = input("Escribe una lista de alturas de estudiantes separados por un espacio \n(no incluyas punto o coma. Ejemplo: 184 178 191 182) \n").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_heights = 0
for  height  in  student_heights:
  total_heights += height
# print(total_heights)

total_students = 0
for  student in student_heights:
  total_students += 1
# print(total_students)

average_student_height = round(total_heights / total_students)
print(f"El promedio de altura de los estudiantes es de {average_student_height} cm")