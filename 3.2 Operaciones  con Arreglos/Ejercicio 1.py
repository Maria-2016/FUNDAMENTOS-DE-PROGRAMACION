# Matriz de 3x3
matriz = [
    [4, 1, 8],
    [5, 12, 3],
    [2, 7, 9]
]

print(matriz)
# Función buscar_valor específico

def buscar_valor(matriz,valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == valor_buscado:
                return i,j

valor_buscado = 12
#print(buscar_valor(matriz,valor_buscado))

if valor_buscado == valor_buscado:
    print("Valor encontrado en la posoción", buscar_valor(matriz,valor_buscado))
else:
    print("Valor incorrecto")

# Si se encontró el valor
# Su posición en la matriz (1,1)