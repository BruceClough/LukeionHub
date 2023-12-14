lecturas = []

while True:
    print("Ingrese el nombre del libro: ")
    lectura_nueva = input("> ")
    lecturas.append(lectura_nueva)

    respuesta = input("Desea agregar otro libro? (si/no): ")
    
    if respuesta.lower() != "si":
        break

print(lecturas)
print("...")
print("Muchas gracias por usar LukeionHub")
