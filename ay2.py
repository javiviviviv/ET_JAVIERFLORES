import csv
import random

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez","Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez","Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

def generar_sueldos():
    sueldos = [random.randrange(300000, 2500000, 1000) for i in range(10)]
    return sueldos

def clasificacion(sueldos):
    st1 = []
    st2 = []
    st3 = []

    for j in range(10):
        if sueldos[j] < 800000:
            st1.append((trabajadores[j], sueldos[j]))
        elif sueldos[j] < 2000000 and sueldos[j] > 800000:
            st2.append((trabajadores[j], sueldos[j]))
        elif sueldos[j] > 2000000:
            st3.append((trabajadores[j], sueldos[j]))
    print("")
    print("Sueldos menores a $800,000")
    print("TOTAL:", len(st1))
    print("Nombre empleado   Sueldo")
    for nombre, sueldo in st1:
        print(f"{nombre:<20} ${sueldo:>8}")

    print("")
    print("Sueldos entre $800,000 y $2,000,000")
    print("TOTAL:", len(st2))
    print("Nombre empleado   Sueldo")
    print("")
    for nombre, sueldo in st2:
        print(f"{nombre:<20} ${sueldo:>8}")

    print("")
    print("Sueldos superiores a $2,000,000")
    print("TOTAL:", len(st3))
    print("Nombre empleado   Sueldo")
    print("")
    for nombre, sueldo in st3:
        print(f"{nombre:<20} ${sueldo:>8}")

    total_sueldos = sum(sueldos)
    print("TOTAL SUELDOS: $", total_sueldos)

def estadisticas(sueldos):
    alto = max(sueldos)
    bajo = min(sueldos)
    prom = sum(sueldos) / len(sueldos)

    media_geometrica = 1
    for sueldo in sueldos:
        media_geometrica *= sueldo
    media_geometrica **= (1 / len(sueldos))

    print("\nEstadísticas de Sueldos:")
    print("Sueldo más alto:", alto)
    print("Sueldo más bajo:", bajo)
    print("Promedio de sueldos:", prom)
    print("Media geométrica de sueldos:", media_geometrica)

def reporte(sueldos):
    print("\nReporte de Sueldos:")
    print("Nombre empleado         Sueldo Base     Descuento Salud   Descuento AFP    Sueldo Líquido")
    with open('reporte_sueldos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        for i in range(10):
            base = sueldos[i]
            salud = base * 0.07
            afp = base * 0.13
            liquido = base - salud - afp
            writer.writerow([trabajadores[i], base, salud, afp, liquido])
            print(f"{trabajadores[i]:<24} ${base:>12,.0f} ${salud:>15,.0f} ${afp:>15,.0f} ${liquido:>15,.0f}")

while True:
    try:
        opc = int(input("\n1. Asignar sueldos aleatorios\n2. Clasificar sueldos\n3. Ver estadísticas.\n4. Reporte de sueldos\n5. Salir del programa\n"))
        if opc == 1:
            sueldos = generar_sueldos()
            print("")
            print("Sueldos generados")

        elif opc == 2:
            clasificacion(sueldos)

        elif opc == 3:
            estadisticas(sueldos)

        elif opc == 4:
            reporte(sueldos)

        elif opc == 5:
            print("Finalizando Programa...")
            print("Desarrollado por Javier Flores Moya")
            print("RUT 22.042.390-5")
            break

        else:
            print("Por favor, indique una opción válida")

    except ValueError:
        print("Por favor, ingrese un número entero válido para la opción")
#Para hacerlo más familiar a los sueldos de Chile usé "randrange", se me hacía muy raro ver que a alguien le pagaban 307095 pesos por ejemplo jeje, si es normal no me descuente porfa