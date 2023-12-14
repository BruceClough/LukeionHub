libros = []

def almacenamiento(libros, respuesta):
    libros.append(respuesta)
    guardar(libros)

def modificar(libros, indice, nueva_respuesta):
    if 0 <= indice < len(libros):
        libros[indice] = nueva_respuesta
        guardar(libros)
    else:
        print("Indice no válido")

def eliminar(libros, indice):
    if 0 <= indice < len(libros):
        del libros[indice]
        guardar(libros)
    else:
        print("Indice no válido")

def agregar ():
    respuestas = []

    print("Ingrese el nombre del libro: ")
    titulo = input("> ")
    respuestas.append(titulo)

    print("Ingrese el autor: ")
    autor = input("> ")
    respuestas.append(autor)

    print("ingrese la fecha de lectura: ")
    fecha_lectura = input("> ")
    respuestas.append(fecha_lectura)

    print("Ingrese un comentario: ")
    comentario = input("> ")
    respuestas.append(comentario)

    return respuestas

def guardar (libros):
    with open("respuestas.txt", "w") as archivo:
        for respuestas in libros:
            archivo.write(str(respuestas) + "\n")

def cargar():
    try:
        with open("respuestas.txt", "r") as archivo:
            lineas = archivo.readlines()
            libros = [eval(linea.strip()) for linea in lineas]
            return libros
    except FileNotFoundError:
        return[]
    
def main():
    libros  = cargar()

    while True:
        print("\n1. Almacenar respuestas")
        print("2. Modificar respuestas")
        print("3. Eliminar respuestas")
        print("4. Agregar elemento")
        print("5. Mostrar respuestas")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            respuesta = agregar()
            almacenamiento(libros, respuesta)
        elif opcion == "2":
            indice = int(input("Ingrese el índice a modificar: "))
            nueva_respuesta = agregar()
            modificar(libros, indice, nueva_respuesta)
        elif opcion == "3":
            indice = int(input("Ingrese el índice a eliminar: "))
            eliminar(libros, indice)
        elif opcion == "4":
            respuesta = agregar()
            almacenamiento(libros, respuesta)
        elif opcion == "5":
            print("Libros registrados")
            for libro, respuestas in enumerate(libros,1):
                print(f"\nLibros {libro}: ")
                print(f"Titulo: {respuestas[0]}, ")
                print(f"Autor: {respuestas[1]}, ")
                print(f"Fecha de lectura: {respuestas[2]}, ")
                print(f"Comentario: {respuestas[3]}")
        elif opcion == "6":
            guardar(libros)
            print("¡Muchas gracias por usar LukeionHub!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
