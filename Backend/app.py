from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from xml.etree import ElementTree as ET
from listas.Cursos import Cursos
from listas.Tutores import Tutores
from listas.Estudiantes import Estudiantes
import utilidades.Utilidades as utl
app = Flask(__name__)
CORS(app)

usuario_actual = None
lista_cursos = Cursos()
lista_tutores = Tutores()
lista_estudiantes = Estudiantes()
asignaciones_tutores = {
    'correcto': 0,
    'incorrecto': 0
    }
asignaciones_estudiantes = {
    'correcto': 0,
    'incorrecto': 0
}

@app.route('/uploadFile', methods=['POST'])
def uploadFile():
    if usuario_actual != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403
    
    if request.method != 'POST':
        return jsonify({'error': 'Method not allowed'}), 405
    
    try:
        file_xml = request.data
        file_decoded = file_xml.decode('utf-8')
        root =  ET.fromstring(file_decoded)
        cursos = root.find('cursos')
        
        # Iteramos sobre la lista de cursos en el XML y agregamos cada curso a la lista
        for curso in cursos:
            nombre = curso.text.strip()
            codigo = curso.get('codigo').strip()
            lista_cursos.agregar_curso(nombre, codigo)
        
        # Obtenemos la lista de tutores del XML
        tutores = root.find('tutores')
        # Iteramos sobre la lista de tutores y los agregamos a la lista del sistema
        for tutor in tutores:
            nombre_tutor = tutor.text.strip()
            id_tutor = tutor.get('registro_personal').strip()
            password = tutor.get('contrasenia').strip()
            lista_tutores.agregar_tutor(id_tutor, nombre_tutor, password)
        
        # Obtenemos la lista de estudiantes del XML
        estudiantes = root.find('estudiantes')
        # Iteramos sobre la lista de estudiantes y los agregamos a la lista del sistema
        for estudiante in estudiantes:
            nombre_estudiante = estudiante.text.strip()
            carnet_estudiante = estudiante.get('carnet').strip()
            password_estudiante = estudiante.get('contrasenia').strip()
            lista_estudiantes.agregar_estudiante(nombre_estudiante, carnet_estudiante, password_estudiante)

        # Obtenemos la lista de asignaciones de tutores y estudiantes
        asignaciones = root.find('asignaciones')

        # Obtenemos las lista de tutores asignados a cada curso
        asignaciones_tutor = asignaciones.find('c_tutores')
        for tutor in asignaciones_tutor:
            codigo_curso = tutor.get('codigo').strip()
            id_tutor = tutor.text.strip()
            nombre_curso = lista_cursos.obtener_nombre_curso(codigo_curso)
            # Verificamos si el tutor existe en la lista de tutores
            existe_tutor = lista_tutores.verificar_tutor(id_tutor)
            # Verificamos si el curso existe en la lista de cursos
            existe_curso = lista_cursos.verificar_curso(codigo_curso)
            if existe_curso and existe_tutor:
                # Asignamos el curso al tutor
                lista_tutores.asignar_curso(id_tutor, codigo_curso, nombre_curso)
                asignaciones_tutores['correcto'] += 1
            else:
                asignaciones_tutores['incorrecto'] += 1

        # Obtenemos las lista de estudiantes asignados a cada curso
        asignaciones_estudiante = asignaciones.find('c_estudiantes')
        for estudiante in asignaciones_estudiante:
            # Obtenemos el código del curso y el carnet del estudiante
            codigo_curso = estudiante.get('codigo').strip()
            carnet_estudiante = estudiante.text.strip()

            existe_estudiante = lista_estudiantes.verificar_estudiante(carnet_estudiante)
            existe_curso = lista_cursos.verificar_curso(codigo_curso)
            # Verificamos si el estudiante y el curso existen
            if existe_estudiante and existe_curso:
                # Asignamos el curso al estudiante
                nombre = lista_cursos.obtener_nombre_curso(codigo_curso)
                lista_estudiantes.asignar_estudiante(carnet_estudiante, codigo_curso, nombre)
                asignaciones_estudiantes['correcto'] += 1
            else:
                asignaciones_estudiantes['incorrecto'] += 1

    except FileNotFoundError:
        print(f"Error: Archivo no encontrado")
    except ET.XMLSyntaxError as e:
        print(f"Error de sintaxis XML: {e}")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

    xml_to_text = utl.return_text(asignaciones_tutores, asignaciones_estudiantes, len(lista_tutores), len(lista_estudiantes))
    return xml_to_text, 200

@app.route('/uploadFile', methods=['DELETE'])
def deleteFile():
    if not usuario_actual == 'admin':
        return jsonify({'error': 'Unauthorized'}), 403
    
    if request.method != 'DELETE':
        return jsonify({'error': 'Method not allowed'}), 405
    
    size_cursos = len(lista_cursos.cursos)
    size_tutores = len(lista_tutores.tutores)
    size_estudiantes = len(lista_estudiantes.estudiantes)

    if size_cursos == 0 and size_tutores == 0 and size_estudiantes == 0:
        return jsonify({'error': 'No hay datos para eliminar'}), 404
    else:
        lista_cursos.delete_all_courses()
        lista_tutores.delete_all_tutor()
        lista_estudiantes.delete_all_students()
        return jsonify({'message': 'Datos eliminados exitosamente'}), 200

    

@app.route('/login', methods=['POST'])
def login():
    global usuario_actual

    if usuario_actual is not None:
        return jsonify({'error': 'Ya hay un usuario autenticado'}), 400
    
    # Obtenemos los datos del usuario desde la solicitud
    data = request.get_json()
    # Extraemos el nombre de usuario y la contraseña
    username = data.get('username')
    password = data.get('password')

    # verificamos la consistencia de los datos
    if not username or not password:
        return jsonify({'error': 'Faltan datos de autenticación'}), 400
    
    if username == 'admin' and password == 'admin':
        usuario_actual = username
        return jsonify({'message': 'Inicio de sesión exitoso',"role":0 }), 200
    

@app.route('/userInformation', methods=['GET'])
def userInformation():
    if not usuario_actual or usuario_actual != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403
    
    if request.method != 'GET':
        return jsonify({'error': 'Method not allowed'}), 405
    
    if len(lista_tutores.tutores) == 0 and len(lista_estudiantes.estudiantes) == 0:
        return jsonify({'error': 'No hay datos disponibles'}), 404
    
    data = utl.merge_list_users(lista_tutores.tutores, lista_estudiantes.estudiantes)
    
    return jsonify(data), 200

@app.route('/log_out', methods=['POST'])
def log_out():

    global usuario_actual
 
    usuario_actual = None
    return jsonify({'message': 'Sesión cerrada exitosamente'}), 200