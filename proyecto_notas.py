import os
menu = ["Agregar tarea", "Eliminar tarea", "Actualizar estado de tarea", "Ver todas las tareas", "Agregar nota", "Eliminar nota", "Actualizar notas", "Ver todas las notas", "Salir"]
menu_activo = True
tareas = {}
notas = {}

def limpiar_pantalla():
     os.system('cls')

def nueva_tarea(tareas):
    print (f"Ha seleccionado {menu[0]}")
    nombre_tarea = input("Ingrese el nombre de la tarea: ")
    estado = input("Ingrese el estado (Pendiente/Completada): ")
    fecha_creacion = input("Ingrese la fecha de creación (YYYY-MM-DD): ")
    prioridad = input("Ingrese la prioridad (Alta/Media/Baja): ")
    tareas[nombre_tarea] = {
            "Estado": estado,
            "Fecha de creación": fecha_creacion,
            "Prioridad": prioridad
        }
    return tareas

def tarea_eli(tareas):
    eliminar = input("¿Qué tarea desea eliminar? Escriba el nombre de la tarea: ")
    valor = tareas.pop(eliminar, None)
    return tareas

def tarea_act(tareas):
    actualizar = input("¿Qué tarea desea actualizar? ")
    estado = input("Ingrese el estado (Pendiente/Completada): ")
    fecha_creacion = input("Ingrese la fecha de creación (YYYY-MM-DD): ")
    prioridad = input("Ingrese la prioridad (Alta/Media/Baja): ")
    tareas[actualizar].update({"Estado": estado, "Fecha de creación": fecha_creacion, "Prioridad": prioridad})
    return tareas

def ver_tareas(tareas):
    for clave, sub_diccionario in tareas.items():
        print(f"{clave}:")
        for sub_clave, valor in sub_diccionario.items():
            print(f"{sub_clave}: {valor}")
    return tareas

def nota_crear(notas):
    nombre_nota = input("Ingrese el nombre de su nota: ")
    categoria = input("Ingrese la categoria (trabajo, personal, estudio): ")
    contenido = input("Contenido de la nota: ")
    fecha_creacion2 = input("Ingrese la fecha de creación (YYYY-MM-DD): ")
    notas[nombre_nota] = {
            "Categoria": categoria,
            "Contenido": contenido,
            "Fecha de creación": fecha_creacion2
        }
    return notas

def nota_eli(notas):
    eliminar1 = input("¿Qué nota desea eliminar? Escriba el nombre de la nota: ")
    valor1 = notas.pop(eliminar1, None)
    return notas

def nota_ver(notas):
    for clave1, sub_diccionario1 in notas.items():
        print(f"{clave1}:")
        for sub_clave1, valor1 in sub_diccionario1.items():
            print(f"{sub_clave1}: {valor1}") 
    return(notas)

def nota_act(notas):
    actualizar1 = input("¿Qué nota desea actualizar? ")
    categoria = input("Ingrese la categoria (trabajo, personal, estudio): ")
    contenido = input("Contenido de la nota: ")
    fecha_creacion2 = input("Ingrese la fecha de creación (YYYY-MM-DD): ")
    notas[actualizar1].update({"Categoria": categoria, "Contenido": contenido, "Fecha de creación": fecha_creacion2})
    return notas 

limpiar_pantalla()
print ("\t*BIENVENIDO AL GESTOR DE TAREAS Y NOTAS*")
while menu_activo:
    print ("\n")
    for menus in menu:
        print(f"{menu.index(menus) + 1}.-{menus}")
    escoger = int(input("\n¿Qué acción desea realizar?\nDigite el número de la operación: ")) 
    if escoger > 9 or escoger < 0:
        limpiar_pantalla()
        print ("Escoja una opcion valida")
    elif escoger == 1:
        limpiar_pantalla()
        nueva_tarea(tareas)
        limpiar_pantalla()
    elif escoger == 2:
        print (f"Ha seleccionado {menu[1]}")
        tarea_eli(tareas)
        limpiar_pantalla()
    elif escoger == 3:
        print (f"Ha seleccionado {menu[2]}")
        tarea_act(tareas)
        limpiar_pantalla()
    elif escoger == 4:
        limpiar_pantalla()
        print (f"Ha seleccionado {menu[3]}\n")
        ver_tareas(tareas)          
    elif escoger == 5:
        print (f"Ha seleccionado {menu[4]}")
        limpiar_pantalla()
        nota_crear(notas)
        limpiar_pantalla()
    elif escoger == 6:
        print (f"Ha seleccionado {menu[5]}")
        nota_eli(notas)
        limpiar_pantalla()
    elif escoger == 7:
        print (f"Ha seleccionado {menu[6]}")
        nota_act(notas)
        limpiar_pantalla()
    elif escoger == 8:
        limpiar_pantalla()
        print (f"Ha escogido {menu[7]}")
        nota_ver(notas)             
    elif escoger == 9:
        limpiar_pantalla()
        print ("Ha seleccionado finalizar programa")
        print ("FIN DEL PROGRAMA...")
        menu_activo = False
