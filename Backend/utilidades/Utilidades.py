from xml.dom import minidom
import re
def return_text(asignaciones_tutores, asignaciones_estudiantes, numero_tutores, numero_estudiantes):

    document = minidom.Document()
    # Crear el elemento raíz
    configuraciones = document.createElement('configuraciones_aplicadas')
    #agregamos el  elemento configuraciones al documento
    document.appendChild(configuraciones)
    # Creamos el elemento tutores_cargados
    tutores_cargados = document.createElement('tutores_cargados')
    # Añadimos el texto de los tutores cargados
    tutores_cargados.appendChild(document.createTextNode(str(numero_tutores)))
    # Añadimos el elemento tutores_cargados al elemento configuraciones
    configuraciones.appendChild(tutores_cargados)

    estudiantes_cargados = document.createElement('estudiantes_cargados')
    estudiantes_cargados.appendChild(document.createTextNode(str(numero_estudiantes)))
    configuraciones.appendChild(estudiantes_cargados)
    
    # Creamos el elemento asignaciones
    asignaciones = document.createElement('asignaciones')
    # Añadimos el elemento total
    # Creamos el elemento 
    tutores = document.createElement('tutores')
    # Creamos el elemento total
    total = document.createElement('total')
    # Añadimos el texto del total de tutores asignados
    total.appendChild(document.createTextNode(str(len_dictionary(asignaciones_tutores))))
    # Añadimos el elemento total al elemento tutores
    tutores.appendChild(total)
    # Iteramos sobre el diccionario de asignaciones de tutores
    for key, value in asignaciones_tutores.items():
        element = document.createElement(key)
        element.appendChild(document.createTextNode(str(value)))
        tutores.appendChild(element)
    # Añadimos el elemento tutores al elemento asignaciones    
    asignaciones.appendChild(tutores)
    # Creamos el elemento estudiantes
    estudiantes = document.createElement('estudiantes')
    # Creamos el elemento total
    total_estudiantes = document.createElement('total')
    # Añadimos el texto del total de estudiantes asignados
    total_estudiantes.appendChild(document.createTextNode(str(len_dictionary(asignaciones_estudiantes))))
    # Añadimos el elemento total al elemento estudiantes
    estudiantes.appendChild(total_estudiantes)
    # Iteramos sobre el diccionario de asignaciones de estudiantes
    for key, value in asignaciones_estudiantes.items():
        element = document.createElement(key)
        element.appendChild(document.createTextNode(str(value)))
        estudiantes.appendChild(element)
    # Añadimos el elemento estudiantes al elemento asignaciones
    asignaciones.appendChild(estudiantes)
    # Añadimos el elemento asignaciones al elemento configuraciones
    configuraciones.appendChild(asignaciones)
    # Formateamos el documento
    formatted_xml = document.toprettyxml(indent="  ")
    return formatted_xml


def len_dictionary(dictionary):
    contador = 0
    for key in dictionary:
        contador += dictionary[key]
    return contador

def merge_list_users(tutores, estudiantes):
    merged_dict = {}
    
    for tutor in tutores:
        merged_dict[tutor.id_tutor] = {
            'nombre': tutor.nombre,
            'password': tutor.password
        }
    for estudiante in estudiantes:
        merged_dict[estudiante.carnet] = {
            'nombre': estudiante.nombre,
            'password': estudiante.password
        }
    return merged_dict

def getHorarios(cadena):
    patron = r'HorarioI:\s*(\d{2}:\d{2})\s*HorarioF:\s*(\d{2}:\d{2})'
    match = re.search(patron, cadena)
    hora_inicio = None
    hora_fin = None
    if match:
        hora_inicio = match.group(1)
        hora_fin = match.group(2)

        if hora_inicio is None or hora_fin is None:
            temp = cadena.split(' ')
            contador =0
            for word in range(temp):
                if 'HorarioI:' == word:
                    hora_inicio = temp[contador + 1]
                elif 'HorarioF:' == word:
                    hora_fin = temp[contador + 1]
                
                if hora_inicio is not None and hora_fin is not None:
                    break
                contador += 1
    else:
        temp = cadena.split(' ')
        contador = 0
        for word in temp:
            if 'HorarioI:' == word:
                hora_inicio = temp[contador + 1]
            elif 'HorarioF:' == word:
                hora_fin = temp[contador + 1]
            
            if hora_inicio is not None and hora_fin is not None:
                break
            contador += 1

    return hora_inicio, hora_fin