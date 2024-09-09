#Tarea: Iteración de arreglos multidimensionales con bucles anidados
"""Crear una matriz 3D que represente los datos de temperaturas diarias en varias ciudades. En una dimensión, puedes tener diferentes ciudades, en otra dimensión, días de la semana (Lunes, Martes, Miércoles, etc.), y en la tercera dimensión, semanas.
Dentro de cada celda de la matriz, puedes almacenar las temperaturas diarias para una ciudad en un día específico de una semana determinada.
Utilizar bucles anidados para calcular el promedio de temperaturas para una ciudad por cada una de las semanas.
Mostrar el promedio de temperaturas para cada ciudad y semana en la pantalla"""
# CREAR LA MATRIZ EN 3D

# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 23},
            {"day": "Sábado", "temp": 23},
            {"day": "Domingo", "temp": 27}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 35},
            {"day": "Jueves", "temp": 34},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 35},
            {"day": "Domingo", "temp": 31}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 34}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 31}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 35},
            {"day": "Martes", "temp": 34},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 29}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 34},
            {"day": "Martes", "temp": 33},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 33}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 33},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 20}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 32}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 34},
            {"day": "Domingo", "temp": 21}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 33},
            {"day": "Miércoles", "temp": 35},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 33}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 30}
        ]
    ]
]

# Calcular el promedio de temperaturas por ciudad y semana
promedios_por_ciudad = []

# Iterar a través de las ciudades, semanas y días para calcular el promedio de temperaturas
for ciudad in temperaturas:  # Iterar sobre cada ciudad en temperaturas
    promedio_semanal = []
    suma_total = 0
    cantidad_total = 0
    for semana in ciudad:  # Iterar sobre cada semana en la ciudad
        suma_semanal = 0
        cantidad_semanal = 0
        for dia in semana:  # Iterar sobre cada día en la semana
            suma_semanal += dia['temp']
            cantidad_semanal += 1
            suma_total += dia['temp']
            cantidad_total += 1
        promedio = suma_semanal / cantidad_semanal  # Calcular el promedio de la semana
        promedio_semanal.append(promedio)
    promedio_ciudad = suma_total / cantidad_total  # Calcular el promedio de la ciudad
    promedios_por_ciudad.append((promedio_semanal, promedio_ciudad))

for i, (promedio_semanal, promedio_ciudad) in enumerate(promedios_por_ciudad):
    print(f"\nCiudad {i + 1}:")
    print(f"Promedio general de la ciudad: {promedio_ciudad:.2f}" "°C")
    for j, promedio in enumerate(promedio_semanal):
        print(f"Promedio de la Semana {j + 1}: {promedio:.2f}" "°C")

