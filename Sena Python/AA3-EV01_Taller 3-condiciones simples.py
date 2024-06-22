# TALLER 3 PYTHON
# AUTOR(A): Carolina Mendoza Vivas
# FECHA: Septiembre 27 / 2022

from datetime import date
hoy= date.today()
print("Hoy es el día: ",hoy)

print("EJERCICIOS USO CONDICIONAL SIMPLE IF - ELSE")
print()
print("EJERCICIO 1")
a=int(input("Digite el valor de A: "))
b=int(input("Digite el valor de B: "))

if a>=b:
    print("A(",a,") es MAYOR o igual que B(",b,")")
else:
    print("A(",a,") es MENOR que B(",b,")")
print()


print("EJERCICIO 2")
curso1="Requerimientos"
curso2="Algoritmos"
print("El curso 1 es: ",curso1)
print("El curso 2 es: ",curso2)
print()
if curso1=="Requerimientos" and curso2=="Algoritmos":
    print("Usted estudia Programación de Software")
else:
    print("Usted estudia otro programa diferente a Programación de Software")
print()

print("EJERCICIO 3")
print("***   Final de Análisis de formación del SENA   ***")
print()
frase=input("Digite una oración: ")
print("La frase en mayúscula es: ",frase.upper())
longitud=len(frase)
print("La longitud de la frase es: ",longitud," caracteres")
if longitud>10:
    print("La frase tiene mas de 10 caracteres")
else:
    print("La frase tiene menos de 10 caracteres")
print()
print("F I N")
