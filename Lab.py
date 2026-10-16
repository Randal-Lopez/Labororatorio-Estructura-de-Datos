from datetime import datetime

# Listas que se utilizan para guardar los datos del programa.
# La cola trabaja con FIFO: el primero en entrar es el primero en salir.
pasajeros = []

# La pila trabaja con LIFO: la ultima salida registrada es la primera en salir.
salidas = []


# Funcion para registrar un pasajero en la cola.
def registrar_pasajero():
    nombre = input("Ingrese el nombre del pasajero: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacio.")
        return

    pasajeros.append(nombre)
    print("Pasajero registrado correctamente.")


# Funcion para atender al primer pasajero de la cola.
def atender_pasajero():
    if len(pasajeros) == 0:
        print("No hay pasajeros pendientes de atender.")
        return

    nombre = pasajeros.pop(0)
    print("Pasajero atendido:", nombre)


# Funcion para mostrar los pasajeros pendientes.
def mostrar_pasajeros():
    if len(pasajeros) == 0:
        print("No hay pasajeros registrados.")
        return

    print("\nOrden de atencion de los pasajeros:")

    for i, nombre in enumerate(pasajeros, start=1):
        print(f"{i}. {nombre}")

    print("Total de pasajeros pendientes:", len(pasajeros))


# Funcion para registrar una salida de bus en la pila.
def registrar_salida():
    codigo = input("Ingrese el codigo del bus: ").strip()
    destino = input("Ingrese el destino del bus: ").strip()
    hora_salida = input("Ingrese la hora de salida (HH:MM): ").strip()

    if codigo == "" or destino == "" or hora_salida == "":
        print("Todos los campos son obligatorios.")
        return

    # Se revisa que el codigo del bus no este registrado en la pila.
    for salida in salidas:
        if salida["codigo"].lower() == codigo.lower():
            print("Ese codigo de bus ya esta registrado.")
            return

    # Se valida que la hora tenga el formato correcto.
    try:
        datetime.strptime(hora_salida, "%H:%M")
    except ValueError:
        print("La hora no es valida. Utilice el formato HH:MM.")
        return

    # Se guarda la fecha y hora en que se registro la salida.
    fecha_registro = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Se guarda toda la informacion de la salida en un diccionario.
    salida = {
        "codigo": codigo,
        "destino": destino,
        "hora_salida": hora_salida,
        "fecha_registro": fecha_registro
    }

    # La salida se agrega al final de la pila.
    salidas.append(salida)
    print("Salida de bus registrada correctamente.")


# Funcion para quitar la ultima salida registrada.
def deshacer_salida():
    if len(salidas) == 0:
        print("No hay salidas registradas.")
        return

    # pop() elimina la ultima salida agregada a la pila.
    salida = salidas.pop()

    print("Se elimino la ultima salida registrada.")
    print("Codigo del bus:", salida["codigo"])
    print("Destino:", salida["destino"])


# Funcion para mostrar las salidas registradas.
def mostrar_salidas():
    if len(salidas) == 0:
        print("No hay salidas registradas.")
        return

    print("\nSalidas de buses registradas:")

    # Se muestran las salidas desde la ultima registrada hasta la primera.
    for i, salida in enumerate(reversed(salidas), start=1):
        print(f"\nSalida {i}")
        print("Codigo del bus:", salida["codigo"])
        print("Destino:", salida["destino"])
        print("Hora programada:", salida["hora_salida"])
        print("Fecha de registro:", salida["fecha_registro"])

    print("\nTotal de salidas registradas:", len(salidas))

    # La ultima salida de la lista es la que esta en la cima de la pila.
    ultima_salida = salidas[-1]
    print("\nUltima salida registrada:")
    print("Codigo del bus:", ultima_salida["codigo"])
    print("Destino:", ultima_salida["destino"])


# Clase que representa cada nodo del arbol de destinos.
class NodoDestino:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []


# Funcion recursiva para mostrar los destinos del arbol.
def mostrar_arbol(nodo, nivel=0):
    print("  " * nivel + nodo.nombre)

    # Se recorre cada hijo para mostrar los destinos que dependen del nodo.
    for hijo in nodo.hijos:
        mostrar_arbol(hijo, nivel + 1)


# Funcion recursiva para buscar un destino en el arbol.
def buscar_destino(nodo, nombre):
    # Si el nombre coincide, se devuelve el nodo encontrado.
    if nodo.nombre.lower() == nombre.lower():
        return nodo

    # Si no coincide, se busca en los hijos del nodo actual.
    for hijo in nodo.hijos:
        resultado = buscar_destino(hijo, nombre)

        if resultado is not None:
            return resultado

    # Si no se encuentra el destino, se devuelve None.
    return None


# Construccion del arbol de destinos.
terminal = NodoDestino("Terminal Central")

zona_oriental = NodoDestino("Zona Oriental")
zona_central = NodoDestino("Zona Central")
zona_occidental = NodoDestino("Zona Occidental")

# Las zonas se agregan como hijos de la terminal.
terminal.hijos.append(zona_oriental)
terminal.hijos.append(zona_central)
terminal.hijos.append(zona_occidental)

# Destinos de la Zona Oriental.
zona_oriental.hijos.append(NodoDestino("San Miguel"))
zona_oriental.hijos.append(NodoDestino("Quelepa"))
zona_oriental.hijos.append(NodoDestino("Jucuapa"))
zona_oriental.hijos.append(NodoDestino("Platanar"))
zona_oriental.hijos.append(NodoDestino("La Coquera"))
zona_oriental.hijos.append(NodoDestino("Moncagua"))
zona_oriental.hijos.append(NodoDestino("Centro"))
zona_oriental.hijos.append(NodoDestino("UNIVO"))
zona_oriental.hijos.append(NodoDestino("UGB"))

# Destinos de la Zona Central.
zona_central.hijos.append(NodoDestino("San Salvador"))
zona_central.hijos.append(NodoDestino("La Libertad"))
zona_central.hijos.append(NodoDestino("Metrocentro"))
zona_central.hijos.append(NodoDestino("Satelite"))
zona_central.hijos.append(NodoDestino("Molino"))
zona_central.hijos.append(NodoDestino("UNAB"))

# Destinos de la Zona Occidental.
zona_occidental.hijos.append(NodoDestino("Volcan"))


# Funcion para consultar un destino.
def consultar_destino():
    print("\nArbol de destinos disponibles:")
    mostrar_arbol(terminal)

    nombre = input("\nIngrese el nombre del destino que desea buscar: ").strip()

    if nombre == "":
        print("Debe ingresar el nombre de un destino.")
        return

    resultado = buscar_destino(terminal, nombre)

    if resultado is not None:
        print("El destino se encuentra registrado:", resultado.nombre)
    else:
        print("El destino no se encuentra registrado.")


# Menu principal del programa.
def menu():
    while True:
        print("\nSISTEMA DE CONTROL DE TERMINAL DE BUSES")
        print("1. Registrar pasajero")
        print("2. Atender pasajero")
        print("3. Mostrar pasajeros pendientes")
        print("4. Registrar salida de bus")
        print("5. Deshacer ultima salida")
        print("6. Mostrar salidas registradas")
        print("7. Mostrar arbol de destinos")
        print("8. Buscar destino")
        print("9. Salir")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_pasajero()

        elif opcion == "2":
            atender_pasajero()

        elif opcion == "3":
            mostrar_pasajeros()

        elif opcion == "4":
            registrar_salida()

        elif opcion == "5":
            deshacer_salida()

        elif opcion == "6":
            mostrar_salidas()

        elif opcion == "7":
            mostrar_arbol(terminal)

        elif opcion == "8":
            consultar_destino()

        elif opcion == "9":
            print("Programa finalizado.")
            break

        else:
            print("Opcion no valida. Intente nuevamente.")


# Se ejecuta el menu principal.
menu()