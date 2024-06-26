import random
import statistics
import csv
from math import prod

def generar_saldos(nombres):
    saldos = {nombre: random.randint(1000, 5000) for nombre in nombres}
    return saldos

def clasificar_saldos(saldos):
    bajos = {nombre: saldo for nombre, saldo in saldos.items() if saldo < 2000}
    medios = {nombre: saldo for nombre, saldo in saldos.items() if 2000 <= saldo < 3500}
    altos = {nombre: saldo for nombre, saldo in saldos.items() if saldo >= 3500}
    return bajos, medios, altos

def calcular_media_geometrica(saldos):
    return int(prod(saldos) ** (1 / len(saldos)))

def calcular_estadisticas(saldos):
    saldo_mas_alto = max(saldos.values())
    saldo_mas_bajo = min(saldos.values())
    saldo_promedio = int(statistics.mean(saldos.values()))
    media_geometrica = calcular_media_geometrica(saldos.values())
    return saldo_mas_alto, saldo_mas_bajo, saldo_promedio, media_geometrica

def generar_reporte(saldos, filename='reporte_saldos.csv'):
    deducciones = {
        'impuesto': 0.15,
        'seguro': 0.05,
        'otros': 0.02
    }
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Cliente', 'Saldo Bruto', 'Impuesto', 'Seguro', 'Otros', 'Saldo Neto'])

        for nombre, saldo in saldos.items():
            impuesto = round(saldo * deducciones['impuesto'])
            seguro = round(saldo * deducciones['seguro'])
            otros = round(saldo * deducciones['otros'])
            saldo_neto = saldo - impuesto - seguro - otros

            writer.writerow([nombre, saldo, impuesto, seguro, otros, saldo_neto])

def mostrar_menu():
    print("Menú de Opciones:")
    print("1. Asignar saldos aleatorios")
    print("2. Clasificar saldos")
    print("3. Ver estadísticas")
    print("4. Generar reporte de saldos")
    print("5. Salir")

def ejecutar_opcion(opcion, saldos, nombres):
    if opcion == '1':
        saldos.clear()
        saldos.update(generar_saldos(nombres))
        print("Saldos generados:")
        for nombre, saldo in saldos.items():
            print(f'{nombre}: {saldo}')
    elif opcion == '2':
        if saldos:
            bajos, medios, altos = clasificar_saldos(saldos)
            print("Saldos bajos:")
            for nombre, saldo in bajos.items():
                print(f'{nombre}: {saldo}')
            print("Saldos medios:")
            for nombre, saldo in medios.items():
                print(f'{nombre}: {saldo}')
            print("Saldos altos:")
            for nombre, saldo in altos.items():
                print(f'{nombre}: {saldo}')
        else:
            print("Primero genere los saldos (opción 1).")
    elif opcion == '3':
        if saldos:
            saldo_mas_alto, saldo_mas_bajo, saldo_promedio, media_geometrica = calcular_estadisticas(saldos)
            print(f"Saldo más alto: {saldo_mas_alto}")
            print(f"Saldo más bajo: {saldo_mas_bajo}")
            print(f"Saldo promedio: {saldo_promedio}")
            print(f"Media geométrica: {media_geometrica}")
        else:
            print("Primero genere los saldos (opción 1).")
    elif opcion == '4':
        if saldos:
            generar_reporte(saldos)
            print("Reporte generado: reporte_saldos.csv")
        else:
            print("Primero genere los saldos (opción 1).")
    elif opcion == '5':
        print("Gracias por usar el programa. ¡Hasta luego!")
        return False
    else:
        print("Opción no válida. Intente de nuevo.")
    return True

def main():
    nombres = ['Ana', 'Luis', 'Marta', 'Pedro', 'Juan', 'Laura', 'Sofía', 'Carlos', 'Andrés', 'María']
    saldos = {}
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if not ejecutar_opcion(opcion, saldos, nombres):
            break

if __name__ == "__main__":
    main()