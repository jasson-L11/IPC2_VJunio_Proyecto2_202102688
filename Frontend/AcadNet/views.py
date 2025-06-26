from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import XMLContentForm, LoginForm
import requests
import pdb

url_backend = 'http://127.0.0.1:5000'

# Create your views here.
def index(request):
    return render(request, 'Login.html')

def iniciarSesion(request):
    try:
        if request.method == 'POST':
            # creamos una instancia del formulario con los datos del request
            form = LoginForm(request.POST)
            # validamos el formulario
            if form.is_valid():
                # si el formulario es válido, procesamos los datos
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                data = {
                    'username': username,
                    'password': password
                }
                response = requests.post(f'{url_backend}/login', json=data)
                response_json = response.json()
                if response.status_code == 200:
                    
                    # Verificamos el rol del usuario
                    rol = int(response_json['role'])

                    if rol == 0:
                        print(f"Usuario {username} autenticado con rol de administrador")
                        # si el rol es 1, redirigimos al usuario a la página de administración
                        redirect_url = redirect('dashboard')
                        redirect_url.set_cookie('user', username)
                        return redirect_url

                else:
                    # si la respuesta no es exitosa, retornamos un error
                    return HttpResponse(f'Error al iniciar sesión: {response_json.get("message", "Unknown error")}', status=response.status_code)

                
                # retornamos una respuesta HTTP de éxito
                return HttpResponse('Inicio de sesión exitoso')
        pass
    except Exception as e:
        print(f"Error: Error al iniciar sesión {e}")
        return HttpResponse('Error al iniciar sesión', status=500)


def previewXML(request):
    if request.method == 'POST':
        # creamos una instancia del formulario con los datos del request
        form = XMLContentForm(request.POST, request.FILES)
        # validamos el formulario
        if form.is_valid():
            # si el formulario es válido, procesamos el archivo XML
            file = request.FILES['file']
            # leemos el contenido del archivo XML
            xml_content = file.read().decode('utf-8')
        
        # retornamos una respuesta HTTP con el contenido XML
    return render(request, 'load_file.html', {'xml_content': xml_content})
    

def dashboard(request):
    try:
        if request.COOKIES.get('user'):
            username = request.COOKIES.get('user')
            return render(request, 'dashboard.html', {'username': username})
        else:
            return redirect('iniciarSesion')
        
    except Exception as e:
        print(f"Error: Error al cargar el dashboard {e}")
        return HttpResponse('Error al cargar el dashboard', status=500)
    

def loadFile(request):
    try:
        return render(request, 'load_file.html')
    except Exception as e:
        print(f"Error: Error al cargar el archivo {e}")
        return HttpResponse('Error al cargar el archivo', status=500)


def sendFile(request):
    # Declaramos las variables para el contenido del XML y el mensaje de respuesta
    response_message = ''
    xml_content = None

    # Verificamos si el método de la solicitud es POST
    if request.method == 'POST':
        xml_content = request.POST.get('xml_content','')
        if xml_content:
            try:
                # Definimos los headers para la solicitud 
                headers = {'Content-Type': 'application/xml'}
                encode_xml_content = xml_content.encode('utf-8')
                # Enviamos la solicitud POST al backend con el contenido XML
                response = requests.post(f'{url_backend}/uploadFile', data=encode_xml_content, headers=headers)
                # Verificamos el código de estado de la respuesta
                if response.status_code == 200:
                    response_message = 'Archivo XML procesado correctamente'

                    #Verificamos el tipo de contenido de la respuesta
                    response_message = response.text
                else:
                    response_message = 'Error al procesar el archivo XML'

            except Exception as e:
                print(f"Error: Error al procesar el contenido XML {e}")
                response_message = 'Error al procesar el contenido XML'
    
        return render(request, 'load_file.html', {'response': response_message, 'xml_content': xml_content})
    

def cleanSystem(request):
    try:
        if request.method == 'GET':
            # Enviamos una solicitud DELETE al backend para eliminar los datos
            response = requests.delete(f'{url_backend}/uploadFile')
            if response.status_code == 200:
                message = response.json()['message']
                return render(request, 'load_file.html', {'xml_content': message})
            elif response.status_code == 404:
                error = response.json()['error']
                return render(request, 'load_file.html', {'xml_content': error})
    except Exception as e:
        print(f"Error: Error al eliminar los datos {e}")
        return render(request, 'load_file.html', {'xml_content': 'Error al eliminar los datos'})
    
def about(request):
    try:
        return render(request, 'about.html')
    except Exception as e:
        print(f"Error: Error al cargar la página de información {e}")
        return render(request, 'dashboard.html', {'error': 'Error al cargar la página de información'})
    
def informationSystem(request):
    try:
        if request.method == 'GET':
            # Enviamos una solicitud GET al backend para obtener la información del sistema
            response = requests.get(f'{url_backend}/userInformation')
            if response.status_code == 200:
                data = response.json()

                return render(request, 'file_information.html',{'data': data})
            else:
                return render(request, 'information_system.html', {'error': 'Error al obtener la información del sistema'})
    except Exception as e:
        print(f"Error: Error al obtener la información del sistema {e}")
        return render(request, 'dashboard.html', {'error': 'Error al obtener la información del sistema'})


def logout(request):
    try:
        
        response = requests.post(f'{url_backend}/log_out')
        
        if response.status_code != 200:
            return HttpResponse('Error al cerrar sesión', status=500)
        
        response = redirect('index')
        response.delete_cookie('user')
        return response

    except Exception as e:
        print(f"Error: Error al cerrar sesión {e}")
        return HttpResponse('Error al cerrar sesión', status=500)