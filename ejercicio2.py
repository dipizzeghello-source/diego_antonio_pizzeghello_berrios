camarotes_disponibles = 90
historial_reservas = 0
opcion = 0

print("¡Bienvenido al sistema de gestión de camarotes del Crucero Atlántico!")

while opcion != 5:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1.- Camarotes disponibles.")
    print("2.- Reservar camarote.")
    print("3.- Cancelar camarote.")
    print("4.- Historial de reservas.")
    print("5.- Salir.")

    try:
        opcion = int(input("Ingrese una opción: \n"))
    except:
        print("Ha ocurrido un error. Por favor ingrese un número válido.")
        opcion = 0
        continue

    if opcion == 1:
        print(f"Camarotes disponibles actualmente: {camarotes_disponibles}")

    elif opcion == 2:
        try:
            cantidad = int(input("Ingrese la cantidad de camarotes a reservar: \n"))
            if cantidad <= 0:
                print("Error: La cantidad a reservar debe ser mayor a 0.")
            elif cantidad > camarotes_disponibles:
                print(f"No hay suficiente capacidad disponible. Solo quedan {camarotes_disponibles} camarotes.")
            else:
                camarotes_disponibles -= cantidad
                historial_reservas += cantidad
                print(f"¡Reserva exitosa! Se han reservado {cantidad} camarote(s).")
        except:
            print("Ha ocurrido un error. Debe ingresar un número entero.")

    elif opcion == 3:
        try:
            cantidad = int(input("Ingrese la cantidad de camarotes a cancelar: \n"))
            if cantidad <= 0:
                print("Error: La cantidad a cancelar debe ser mayor a 0.")
            elif (camarotes_disponibles + cantidad) > 90:
                print("Error: La cancelación supera la capacidad máxima permitida del crucero (90 camarotes).")
            else:
                camarotes_disponibles += cantidad
                historial_reservas -= cantidad
                print(f"Cancelación exitosa. Se han liberado {cantidad} camarote(s).")
        except:
            print("Ha ocurrido un error. Debe ingresar un número entero.")

    elif opcion == 4:
        print(f"Total de reservas activas durante la sesión: {historial_reservas}")

    elif opcion == 5:
        print("Gracias por utilizar nuestro software, hasta la próxima.")
    else:
        print("Opción no válida. Por favor seleccione entre 1 y 5.")