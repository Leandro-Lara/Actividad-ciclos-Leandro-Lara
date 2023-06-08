print("Bienvenido")
number=int(input("Ingrese el numero de el cual desea ver el factorial :"))
factorial=1
for _ in range(1, number+1):
  factorial*=_
print("El valor factorial de",number, "es:",factorial)