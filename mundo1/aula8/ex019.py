# Sorteio de alunos

# COM RADINT
'''from random import randint
student = []
for i in range (4):
  name = input("Digite o nome do aluno: ")
  student.append(name)
print(f'O aluno sorteado é: {student[randint(0,4)]}')'''

# COM CHOICE
from random import choice
student = []
for i in range (4):
  name = input("Digite o nome do aluno: ")
  student.append(name)
print(f'O aluno sorteado é: {choice(student)}')