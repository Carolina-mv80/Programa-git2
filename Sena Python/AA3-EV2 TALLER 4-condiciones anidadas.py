# TALLER 4 PYTHON
# AUTOR(A): Carolina Mendoza Vivas
# FECHA: Septiembre 27 / 2022

from datetime import date
hoy= date.today()
print("Hoy es el día: ",hoy)

print("EJERCICIOS USO CONDICIONAL ANIDADOS IF - ELSE")
print()
print("EJERCICIO 1 - CLASES DE TRIÁNGULOS")
a=int(input("Digite el valor de lado A: "))
b=int(input("Digite el valor de lado B: "))
c=int(input("Digite el valor de lado C: "))

if a==b and a==c and b==c:
    print("El triángulo es EQUILÁTERO")
else:
    if a==b or a==c or b==c:
        print("El triángulo es ISÓCELES")
    else:
        print("El triángulo es ESCALENO")
print()

print("EJERCICIO 2")
animal=input("Digite un animal: ")
animal=animal.upper()

if animal=="PERRO":
    print("Este animal es el mejor amigo del hombre: ",animal)
elif animal=="GATO":
    print("Este animal persigue a los ratones: ",animal)
elif animal=="OSO":
    print("Este animal vive en el Polo Norte: ",animal)
else:
    print("NO es Perro, no es Gato, no es Oso...")

print()
print("F I N")
