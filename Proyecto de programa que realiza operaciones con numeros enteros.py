print("Bienvenido al sistema")
print(" ")
print("Por favor, inicie sesion para continuar")
print("")

nombre = str(input("Ingrese su nombre:" + " "))
matricula = int(input("Digite su matricula: "))
while matricula < 9999999 or matricula > 100000000:
	matricula = int(input("Para inciar sesion, la matricula debe tener 8 digitos"))
	validar = int(input("Por favor valide su matricula:" + " "))
	while validar < 9999999 or validar > 10000000:
		validar  = int(input("La matricula debe tener 8 digitos:"))
	while validar != matricula:
		validar = int(input("Los datos de la matricula no coinciden"))
		print("")
print("Bienvenid", nombre, "Su ID es", matricula)
print("")

print("Leer dos numeros enteros y mostrar todos los enteros comprendidos entre ellos")
print("")

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese el segundo numero: "))

enteros = 0
print("")

if num1 < num2:
	print("Totodos los enteros comprendidos entre", num1, "y", num2, "son:")
	for enteros in range (num2+1,num1):
		print(enteros)
input("Fin")

print("Leer dos numeros y mostrar todos los numeros terminados en 4, entre esos dos numeros")

numero1 = int(input("Ingrese un numero"))
numero2 = int(input("Ingrese el segundo numero"))
 terminados = 0

 print("Todos los numeros terminados en 4 entre", numero1, "y", numero2, "son: ")

 if numero1< numero2:
 	for terminados in range (num1+1,num2);
 	     if terminados%10 == 4:
 	     	print(termiandos)
 
 if numero2 < numero1:
 	for terminados in range(num2+1,num1):
 		if termiandos%10==4:
 			print(terminados)
input("Fin")







