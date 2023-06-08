print("Numeros primos")
numerolimite = int(input("Ingrese un número: "))
print(f"Números primos hasta {numerolimite}:")
for i in range(2, numerolimite + 1):
    es_primo = True
    for divisor in range(2, int(i ** 0.5) + 1):
        if i % divisor == 0:
            es_primo = False
            break
    if es_primo:
        print(i)