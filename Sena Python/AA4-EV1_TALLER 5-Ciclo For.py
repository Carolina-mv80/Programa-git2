# TALLER 5 PYTHON
# AUTOR(A): Carolina Mendoza Vivas
# FECHA: Septiembre 27 / 2022

from datetime import date
hoy= date.today()
print("Hoy es el día: ",hoy)

print("EJERCICIOS CICLOS ITERATIVOS CON LA SENTENCIA FOR ")
print()
print("EJERCICIO 1")
print("Repetición serie entre dos números")
num1=int(input("Digite número 1: "))
num2=int(input("Digite número 2 mayor que número 1: "))

print("Inicio ciclo con incremento de 1")
for i in range(num1, num2+1):
    print(i)
print("Fin ciclo incremento 1")
print()

print("EJERCICIO 2")
print("Inicio ciclo con incremento de 2")
for i in range(num1, num2+1, 2):
    print(i)
print("Fin ciclo incremento 2")
print()

print("EJERCICIO 3")
print("Ciclo deletrear texto")
empresa=input("Digite nombre: ")
empresa=empresa.lower()
for character in empresa:
    print(character)
print("Fin ciclo deletrear")

print()
print("F I N")
