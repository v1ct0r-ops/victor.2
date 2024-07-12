diccionario = {}
  






while True:
    print("MENU")
    print("1.-Agregar un nuevo producto al inventario")
    print("2.-Actualizar la cantidad de un stock de un producto existente")
    print("3.-Actualizar el precio de un producto existente")
    print("4.-Eliminar un producto del inventario")
    print("5.-Mostrar el inventario completo")
    print("6.-Hacer una compra")
    print("7.-Salir del programa")
    print()

    opc = int(input("Ingrese su opcion (1-7):\t"))

    

    if opc == 1:
        fruta = input("Ingrese la fruta que desea agregar:\t")
        cantidad = int(input("Ingrese la cantidad a agregar:\t"))
        precio = int(input("Ingrese el precio a agregar:\t"))

        diccionario[fruta] = {
        "precio":{cantidad},
        "cant":{precio}
        }

        print("Se ha agregado la fruta correctamente")
    elif opc == 2:
        print(diccionario)
    elif opc == 3:
        nombre = input("Ingrese la fruta que busca\t")
        if nombre in diccionario.keys():
            print("El producto se encuentra")
        else:
            print("No se encuentra")

    elif opc == 4:
        pass
    elif opc == 5:
        pass
    elif opc == 6:
        pass
    elif opc == 7:
        break








#agregar






