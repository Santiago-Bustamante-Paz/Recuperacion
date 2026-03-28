def bubble_sort(lista):
    n=len(lista)
    for i in range(n-1):
        for j in range(n-1-i):
            if lista[j]>lista[j+1]:
                lista[j],lista[j+1]=lista[j+1],lista[j]
    return lista
while True:
    try:
        cantidad = int(input("Cuántos números va a ingresar? "))
        if cantidad <=0:
            print("Ingrese un número mayor a 0.")
            continue
        break
    except ValueError:
        print("Inválido. Ingrese un número entero.")
numeros=[]
for i in range(1,cantidad+1):
    while True:
        try:
            num=float(input(f"Ingrese número {i}: "))
            numeros.append(num)
            break
        except ValueError:
            print("Ingrese un número.")
print(f"\nLista original: {numeros}")
ordenada=bubble_sort(numeros.copy())
print(f"Lista ordenada: {ordenada}")