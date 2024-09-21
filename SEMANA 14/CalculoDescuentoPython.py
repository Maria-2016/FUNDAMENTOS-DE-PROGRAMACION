print("SEMANA:14 Tarea de Programación: Cálculo de Descuento en Compras")
# Crear función para el calculo de descuento:
def calcular_descuento(monto_total, porcentaje_descuento=10):

    descuento = monto_total * (porcentaje_descuento / 100)  # Calcular el descuento
    return descuento  # Retornar el descuento calculado

# EJEMPLO 1: Solo se proporciona el monto total, se aplica el descuento predeterminado (10%)
monto1 = 500  # Ejemplo de compra
descuento1 = calcular_descuento(monto1)  # Aplicar el descuento
monto_final1 = monto1 - descuento1  # Calcular el monto final a pagar después del descuento
print("Resultado del EJEMPLO 1 (monto 1)")
# Mostrar los resultados del primer ejemplo:
print(f"Monto total 1: ${monto1}")
print(f"Descuento aplicado: ${descuento1}")
print(f"Monto final a pagar: ${monto_final1}")
print()  # Salto de línea para separar los ejemplos
print("*************************************************************")
# EJEMPLO 2: Se proporciona tanto el monto total como un porcentaje de descuento diferente
monto2 = 3000  # Otro ejemplo de compra
descuento2 = calcular_descuento(monto2, 40)  # Aplicar un descuento del 40%
monto_final2 = monto2 - descuento2  # Calcular el monto final a pagar después del descuento

print("Resultado del EJEMPLO 2 (monto 2)")
# Mostrar los resultados del segundo ejemplo:
print(f"Monto total 2: ${monto2}")
print(f"Descuento aplicado: ${descuento2}")
print(f"Monto final a pagar: ${monto_final2}")

