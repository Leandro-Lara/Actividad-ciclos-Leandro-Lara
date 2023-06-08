print("Bienvenido")

numero= int(input("Ingrese un numero"))
numero2= int(input("Ingrese un numero"))
for l in range(numero + 1):
  for a in range(l, numero2 + 1):
   print(f"{l}-{a}")