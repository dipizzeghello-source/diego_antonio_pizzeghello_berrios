chefs_maestros = 0
chefs_aprendices = 0

cantidad_chefs = 0
while cantidad_chefs <= 0:
    try:
        cantidad_chefs = int(input("¿Cuántos chefs desea registrar?: \n"))
        if cantidad_chefs <= 0:
            print("¡Ingrediente inválido! Ingresa un entero positivo para continuar el registro.")
    except:
        print("¡Ingrediente inválido! Ingresa un entero positivo para continuar el registro.")
        cantidad_chefs = 0

for i in range(cantidad_chefs):
    print(f"--- Registro del Chef #{i + 1} ---\n")
    
    codigo_valido = False
    while not codigo_valido:
        codigo = input("Ingrese el Código Culinario (mín. 8 caracteres, sin espacios): \n")

        if len(codigo) >= 6 and codigo == codigo.replace(" ", ""):
            codigo_valido = True
        else:
            print("Código inválido. Debe tener al menos 8 caracteres y no contener espacios.")

    experiencia = 0
    while experiencia <= 0:
        try:
            experiencia = int(input("Ingrese los años de experiencia culinaria: \n"))
            if experiencia <= 0:
                print("¡Error gastronómico! Ingresa un número entero positivo para la experiencia culinaria.")
        except:
            print("¡Error gastronómico! Ingresa un número entero positivo para la experiencia culinaria.")
            experiencia = 0
                
        if experiencia > 5:
            chefs_maestros += 1
        else:
            chefs_aprendices += 1

print(f"\n¡La escuela cuenta con {chefs_maestros} Chefs Maestros y {chefs_aprendices} Chefs Aprendices! ¡A cocinar!")