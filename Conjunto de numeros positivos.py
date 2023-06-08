aditiion=0
resultado=0
while True:
  number1=int(input("ingrese un valor aleatorio: "))
  number2=int(input("ingrese un valor aleatorio: "))

  if number1==0 or number2==0:
    print("Ejecucion finalizada")
    break
    total = number1+number2
    aditiion+=1
    if aditiion>=0:
      solo=total/aditiion
      print("El promedio de los numeros sumados es de: ",solo)
    else:
      print("ingrese un numero positivo")