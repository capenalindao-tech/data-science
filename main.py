# RETO 1 : Crear  un programa simulador registro de Empresas
import os
from time import sleep
"""
PROYECTO 1: CRUD DE EMPRESA
NOMBRE: CARLOS PEÑA LINDAO
"""

dic_empresas = {
    '100':{
        'rsocial':'TECSUP',
        'direccion' : 'CALLE PERU 123'
    }
}

ANCHO = 50

while(True):
    os.system("clear")
    print(" " * 10 + "GESTIÓN DE EMPRESAS")
    print("="*ANCHO)
    print("""
         [1] Registar Empresa
         [2] Mostar Empresa
         [3] Actualizar Empresa
         [4] Eliminar Empresa
         [5] Salir
          """)
    print("=" * ANCHO)
    opcion = int(input('INGRESE OPCIÓN : '))
    os.system("clear")
    if opcion == 1:
        print("=" * ANCHO)
        print(" " * 10 + "Registar Empresa")
        print("=" * ANCHO)

        ruc = input("Ingrese el RUC: ")
        rsocial = input("Ingrese la Razón Social: ")
        direccion = input("Ingrese la Dirección: ")
        dic_nueva_empresa = {
            'rsocial': rsocial,
            'direccion': direccion
        }
        dic_empresas[ruc] = dic_nueva_empresa
        print("Empresa registrada existosamente")

    elif opcion == 2:
        print("=" * ANCHO)
        print(" " * 10 + "Mostar Empresa")
        print("=" * ANCHO)

        for ruc,info in dic_empresas.items():
            print(f"RUC : {ruc}")
            print(f"Razón Social : {info['rsocial']}")
            print(f"Dirección : {info['direccion']}")
            print('*' * ANCHO)

    elif opcion == 3:
        print("=" * ANCHO)
        print(" " * 10 + "Actualizar Empresa")
        print("=" * ANCHO)

        ruc = input("Ingrese RUC de la empresa a actualizar : ")
        if ruc in dic_empresas:
            print(f"Empresa Encontrada : {dic_empresas[ruc]['rsocial']}")
            nueva_rsocial = input(f"NUEVA RAZÓN SOCIAL({dic_empresas[ruc]['rsocial']}) : ")
            nueva_direccion = input(f"NUEVA DIRECCIÓN({dic_empresas[ruc]['direccion']}) : ")
            if nueva_rsocial:
                dic_empresas[ruc]['rsocial'] = nueva_rsocial
            if nueva_direccion:
                dic_empresas[ruc]['direccion'] = nueva_rsocial
            print("Empresa Actualizada exitosamente!!!")
        else:
            print('No se econtro la empresa para el RUC ingresado')

    elif opcion == 4:
        print("=" * ANCHO)
        print(" " * 10 + "Eliminar Empresa")
        print("=" * ANCHO)

        ruc = input("Ingrese RUC de la empresa a eliminar : ")
        if ruc in dic_empresas:
            del dic_empresas[ruc]
            print('Empresa Eliminada Exitosamente')
        else:
            print('No se econtro la empresa para el RUC ingresado')

    elif opcion == 5:
        print("=" * ANCHO)
        print(" " * 10 + "Saliendo del aplicativo")
        print("=" * ANCHO)
        sleep(2)
        break

    else:
        print("Opcion NO Valida...")
    
    input("Presione ENTER para continuar...")
