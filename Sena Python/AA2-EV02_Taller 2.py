# TALLER 2 PYTHON
# AUTOR(A): Carolina Mendoza Vivas
# FECHA: Septiembre 20 / 2022

from datetime import date
hoy=date.today() # fecha actual
print("Hoy es el día: ", hoy)

print("Ingreso de datos...")
a=int(input("Digite el primer número: "))
b=int(input("Digite el segundo número: "))
c=int(input("Digite el tercer número: "))
print()
print()
x=[a,b,c]
print("Ejemplo funciones con datos enteros...")
print("El valor máximo es = ", max(x))
print("El valor mínimo es = ", min(x))
print("La suma de los números es = ", sum(x))
print()

print("Ejemplo funciones con datos decimales...")
z=float(input("Digite el primer número con decimales: "))
redondo=round(z)
print("El valor digitado es: ", z," y redondeado es: ",redondo)
print()

print("Ejemplos funciones de texto...")
frase=input("Digite una oración con mayúsculas y minúscula: ")
print("La oración en mayúscula es: ", frase.upper())
print("La oración en minúscula es: ", frase.lower())
print("La oración unicia con mayúscula es: ", frase.capitalize())
print("La oración con palabras en mayúscula es: ", frase.title())
print("La longitud de la frase es: ", len(frase), " caracteres")
print()
print("FIN DEL EJERCICIO")
