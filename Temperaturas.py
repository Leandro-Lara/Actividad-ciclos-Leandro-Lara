print("Bienvenido")
g_fahrenheit = float(input("Ingrese la temperatura actual: "))
if g_fahrenheit ==999:
  print("Usted esta ardiendo")
else:
  g_celcius = (g_fahrenheit-32) * (5/9)
  print ("La temperatura ingresada es ", g_celcius, "grados celcius")