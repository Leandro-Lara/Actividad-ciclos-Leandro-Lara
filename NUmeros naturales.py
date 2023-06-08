print("Bienvenido")
numberx = int(input("Ingrese un valor: "))
numberz = int(input("Ingrese un valor: "))
if numberx >= numberz:
  print("El primer valor ingresado no puede ser mayor que el primero")
else:
  for i in range(numberx, numberz +1):
    print("*", i)