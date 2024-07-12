from random import uniform
from statistics import mean
import csv
import random


sueldos = []


def asignar_sueldo_aleatorio():
    sueldo = round(uniform(3000, 25000), 2)
    sueldos.append(sueldo)
    print(f'Se ha asignado un sueldo aleatorio de ${sueldo}')


def clasificar_sueldos():
    sueldos_ordenados = sorted(sueldos)
    print('Sueldos ordenados de menor a mayor:')
    for sueldo in sueldos_ordenados:
        print(f'${sueldo}')


def ver_estadisticas():
    if not sueldos:
        print('Aún no se han asignado sueldos.')
        return
    
    total_sueldos = len(sueldos)
    sueldo_maximo = max(sueldos)
    sueldo_minimo = min(sueldos)
    sueldo_promedio = mean(sueldos)

    print(f'Cantidad de sueldos registrados: {total_sueldos}')
    print(f'Sueldo máximo: ${sueldo_maximo}')
    print(f'Sueldo mínimo: ${sueldo_minimo}')
    print(f'Sueldo promedio: ${sueldo_promedio:.2f}')


def reporte_sueldos():
    if not sueldos:
        print('Aún no se han asignado sueldos.')
        return
    
    print('Reporte de sueldos:')
    for indice, sueldo in enumerate(sueldos, start=1):
        print(f'Sueldo {indice}: ${sueldo}')


def exportar_sueldos(nombre_archivo):
    if not sueldos:
        print('No hay sueldos para exportar.')
        return
    
    try:
        with open(nombre_archivo, 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            for sueldo in sueldos:
                escritor_csv.writerow([sueldo])
        print(f'Se han exportado los sueldos al archivo {nombre_archivo} correctamente.')
    except IOError:
        print(f'Error al intentar escribir en el archivo {nombre_archivo}.')


def importar_sueldos(nombre_archivo):
    global sueldos
    sueldos = []  

    try:
        with open(nombre_archivo, 'r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            for linea in lector_csv:
                sueldo = float(linea[0])
                sueldos.append(sueldo)
        print(f'Se han importado los sueldos desde el archivo {nombre_archivo} correctamente.')
    except IOError:
        print(f'Error al intentar leer el archivo {nombre_archivo}.')


def ejecutar_menu():
    while True:
        print("\n--- Menú ---")
        print("1. Asignar sueldo aleatorio")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Exportar sueldos a CSV")
        print("6. Importar sueldos desde CSV")
        print("7. Salir del programa")

        opcion = input("Ingrese el número de la opción que desea ejecutar: ")

        if opcion == '1':
            asignar_sueldo_aleatorio()
        elif opcion == '2':
            clasificar_sueldos()
        elif opcion == '3':
            ver_estadisticas()
        elif opcion == '4':
            reporte_sueldos()
        elif opcion == '5':
            nombre_archivo = input("Ingrese el nombre del archivo CSV para exportar los sueldos: ")
            exportar_sueldos(nombre_archivo)
        elif opcion == '6':
            nombre_archivo = input("Ingrese el nombre del archivo CSV para importar los sueldos: ")
            importar_sueldos(nombre_archivo)
        elif opcion == '7':
            print("¡ADIOS!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 7.")

if __name__ == "__main__":
    ejecutar_menu()


   
    




