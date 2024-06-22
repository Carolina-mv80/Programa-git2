# TALLER 6 PYTHON
# AUTOR(A): Carolina Mendoza Vivas
# FECHA: Septiembre 27 / 2022

from datetime import date
hoy= date.today()
print("Hoy es el día: ",hoy)

print("EJERCICIOS CICLOS ITERATIVOS CON LA SENTENCIA WHILE ")
print()
print("EJERCICIO 1")
print("Ciclo controlado por contador")
num1=int(input("Digite un número para repetición: "))
i=1
while i<=num1:
    print(i)
    i+=1
print("Fin ciclo while")
print()

print("EJERCICIO 2")
print("Ciclo controlado por evento acertar número secreto")
i=1
num1=5
num2=int(input("Digite número entre 1 o 10: "))
while num2 !=num1:
    i+=1
    num2=int(input("Digite número entre 1 o 10: "))
print("Acertaste el número en el intento No. ",i)
print("Fin ciclo")
print()

print("EJERCICIO 3")
print("Ciclo abortado con la sentencia break al incluir ...A... en nombre")
amistad=input("Digite un nombre: ")
amistad=amistad.upper()
for character in amistad:
    print(character)
    if character =="A":
        break
print("Fin ciclo sentencia break")

print()
print("F I N")
