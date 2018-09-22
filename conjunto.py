
"""Operacion entre conjuntos"""
"""Alexis Eliseo Kauil Dzib"""


from clase_conjunto import Conjuntos

set_one={9,6,5,2,7,10} #Definir un conjunto, empleamos sets
set_two={12,7,4,10,11}


print("Selecciona una opción: ")
print("\t1 - Eliminar un elemento de un conjunto")
print("\t2 - Ingresar un elemento a un conjunto")
print("\t3 - Union de conjuntos")
print("\t4 - interseccion de dos conjuntos")
print("\t5 - diferencia de dos conjuntos")
print("\t6 - Pertenece un elemento a un conjunto")
print("\t7 - conjunto vacio")
print("\t8 - Espacio")
print("\t9 - salir")

prototipo = Conjuntos(set_one,set_two)

while True:

    # solicituamos una opción al usuario

    opcionMenu = input("\ninserte de una opcion>> ")

    if opcionMenu =="1":
        prototipo.eliminar_1()

    elif opcionMenu == "2":
        prototipo.agregar_1()

    elif opcionMenu == "3":
        prototipo.union()

    elif opcionMenu == "4":
        prototipo.interseccion()

    elif opcionMenu == "5":
        prototipo.diferencia_A()

    elif opcionMenu == "6":
        prototipo.verificar_A()

    elif opcionMenu == "7":
        prototipo.conjunto_vacio()

    elif opcionMenu == "8":
        prototipo.espacio()

    elif opcionMenu == "9":
        break

    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")