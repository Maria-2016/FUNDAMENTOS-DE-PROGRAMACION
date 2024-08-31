matriz = [
    [2, 6, 9],
    [1, 8, 2],
    [4, 5, 3]
]

# Metodo de ordenamiento buble_sort

def buble_sort(fila):
    # Algoritmo buble sort
    n = len(fila)
    for i in range(n):
        for j in range(n - 1, i, -1):
            if fila[j] > fila[j - 1]:
                fila[j], fila[j - 1] = fila[j - 1], fila[j]
                print(fila)


print("Matriz original ")
print(matriz)
buble_sort(matriz[1])
print(matriz)