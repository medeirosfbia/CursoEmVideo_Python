# Sorteio de alunos

from random import shuffle
student = []
for i in range (4):
  name = input("Digite o nome do aluno: ")
  student.append(name)

print()
shuffle(student)
for i in range (4):
  print(f'O {i+1}° aluno sorteado é o: {student[i]}')