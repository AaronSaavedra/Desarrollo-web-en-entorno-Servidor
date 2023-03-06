import json
from random import randrange
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import models
from .models import (Clientes, Fotografo, Agencia, Comentarioagencia)
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import get_random_string
from django.core.exceptions import ObjectDoesNotExist

"""
from array import array
from django.db import models
#from django.contrib.auth.hashers import hashpw, gensalt
from django.db.models import Q
#from django.views.decorators.csrf import csrf_exempt
import jwt
import json
import pai.views
import string
import random
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_http_methods
from django.conf import settings
from django.contrib.auth import authenticate

#Crear Usuario
import random
import string
from django.http import JsonResponse
#from django.views.decorators.csrf import csrf_exempt
"""
"""
@csrf_exempt
def create_user(request):
    # Obtener los datos del body del request
    data = json.loads(request.body)
    user_type = data.get('type')
    email = data.get('email')
    nombre = data.get('nombre')
    contrasena = data.get('contrasena')
    CContrasena = data.get('CContrasena')

    # Validar que los datos del request sean válidos
    if not user_type or not email or not nombre or not contrasena or not CContrasena:
        return JsonResponse({'error': 'Faltan datos en el request'}, status=400)
    if contrasena != CContrasena:
        return JsonResponse({'error': 'Las contraseñas no coinciden'}, status=400)

    try:
        token = ''.join(random.choices(string.ascii_letters, k=6))

        # Insertar el nuevo usuario en la base de datos
        if user_type == 'Clientes':
            Cliente = Clientes.objects.create(
                email=email,
                contrasena=contrasena,
                name=nombre,
                token=token
            )
            return JsonResponse({'success': 'Cliente creado correctamente', 'token': token}, status=201)
        elif user_type == 'Fotografo':
            Fotografo = Fotografo.objects.create(
                email=email,
                contrasena=contrasena,
                name=nombre,
                token=token
            )
            return JsonResponse({'success': 'Fotografo creado correctamente', 'token': token}, status=201)
        elif user_type == 'Agencia':
            Agencia = Agencia.objects.create(
                email=email,
                contrasena=contrasena,
                name=nombre,
                token=token
            )
            return JsonResponse({'success': 'Agencia creada correctamente', 'token': token}, status=201)
        else:
            return JsonResponse({'error': 'Tipo de usuario no válido'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    
	
"""
"""
def home (request):
	Maximo_fotografos = Fotografo
	Maximo_agencias = Agencia.objetos.all()
	
	AleatorioFotografo = randrange(1, Maximo_fotografos,1)
	AleatorioAgencia = randrange(1, Maximo_agencias,1)
	
	# Carrusel
	aleatorio = randrange(1,2,1)
	
	if aleatorio==1:
        a=2
		#Metemos imagen y descripcion
	else:
        a=1
    		#Metemos imagen y descripcion
	#
	
Filas = [[0, 0, 0,0,0,0], [0,0]]
numero=0
fuera=0
foto=0
i=0
indice=0
Agencia=0
aleatorio = randrange(1,2,1)
if aleatorio ==1:
	while foto<6:
		AleatorioFotografo=randrange(1,Maximo_fotografos,1)
		while numero<6 and fuera==0:
			for i in 6:
					if Filas(i,1)==AleatorioFotografo:
						fuera=1
					else:
						numero=numero+1
		if numero==6:
			Filas(indice,1)==AleatorioFotografo
			Filas(indice,2)==1#Descripcion 
			foto=foto+1
		indice=indice+1
else:
	while Agencia<6:
		AleatorioAgencia=randrange(1,Maximo_agencias,1)
		while numero<6 and fuera==0:
			for i in 6:
					if Filas(i,1)==AleatorioAgencia:
						fuera=1
					else:
						numero=numero+1
		if numero==6:
			Filas(indice,1)==AleatorioAgencia
			Filas(indice,2)==1#Descripcion 
			foto=foto+1
		indice=indice+1
		
"""

"""
@csrf_exempt
def cambiar_contrasena(request):
	if request.method == "POST":
		#pillamos los datos del body
		json_load =json.loads(request.body)
		#pillamos la contraseña antigua
		contrasenaAntigua=json_load['contrasenaAntigua'] #dentro de los [] metemos el valor en react
		#pillamos la contraseña nueva
		ContrasenaNueva=json_load['ContrasenaNueva']
		#pillamos la repeticion de la contraseña nueva 
		ContrasenaNueva2=json_load['ContrasenaNueva2']

			# Validamos la contraseña
		if ContrasenaNueva!=ContrasenaNueva2:
			return JsonResponse({'error': 'No coinciden'}, status=400)
		else:
			#Cogemos el token en la cabecera
			tokens = request.headers.get('token')
			clientes=Clientes.objects.get(token=tokens)
			if clientes==None:
				return JsonResponse({'error': 'Invalid token'}, status=401)

			else:
				#cliente = Clientes.objects.get(token=tokens ) #seleccionamos el cliente con el token
				if check_password(contrasenaAntigua, cliente.contrasena): #Validamos que la contraseña Antigua es del cliente

						cliente.contrasena=set_password(ContrasenaNueva) #Cambiamos la contraseña
						#sentencias para cambiar la contraseña
						print('contraseña cambiada')
						cliente.save()
				else:
					return JsonResponse({'error': 'contraseña incorrecta'}, status=403)

"""
"""
			#Hacemos lo mismo en fotografos y agencias
			elif Fotografo.objects.get(token=tokens )== None:
				fotografo = Fotografo.objects.get(token=tokens )
				if check_password(contraseñaAntigua, fotografo.contraseña):
						fotografo.contraseña=set_password(ContraseñaNueva)
						#sentencias para cambiar la contraseña
						print('contraseña cambiada')
						fotografo.save()
				else:
					return JsonResponse({'error': 'old_password incorrecta'}, status=403)
			elif Agencia.objects.get(token=tokens )==None:
				agencia = Agencia.objects.get(token=tokens )
				if check_password(contraseñaAntigua, agencia.contraseña):
						agencia.contraseña=set_password(ContraseñaNueva)
						#sentencias para cambiar la contraseña
						print('contraseña cambiada')
						agencia.save()
				else:
					return JsonResponse({'error': 'old_password incorrecta'}, status=403)
	
	
"""
#################################################		
"""
def editar_perfitl(reques):
	#cogemos los datos del cuerpo
	cuerpo =json.loads(request.body)
	#cogemos el token de la cabecera
	tokens = json.loads(request.header)
	if not tokens or tokens != token:
		return JsonResponse({'error': 'Invalid token'}, status=401)
	#Cogemos el cliente con el token
	cliente = Clientes.objects.get(token=tokens )
	#Cogemos el fotografo con el token
	fotografo = Fotografo.objects.get(token=tokens )
	#Cogemos el agencia con el token
	agencia= Agencia.objects.get(token=tokens )
	
#Preguntamos si el cliente esta vacio 
	if cliente!=None:
		#Pillamos lod datos del cuerpo
		editar_NombreUsuario=json['nombreUsuario']
		editar_Descripcion=json['Descripcion']
		editar_numeroTelefono=json['NumeroTelefono']
		editar_usuario=json['usuario']
		editar_correo=json['correo']
		editar_fotoperfil=json['fotoPerfil']
		#Modificamos los datos si no estan vacios, es decir si no se van a modificar
		if editar_NombreUsuario!="":
			cliente.nombre = editar_NombreUsuario #modificamos los datos
		if editar_Descripcion!="":
			cliente.descripcion = editar_Descripcion
		if editar_numeroTelefono!="":
			cliente.telefono = editar_numeroTelefono
		if editar_usuario!="":
			cliente.usuario = editar_usuario
		if editar_correo!="":
			cliente.email = editar_correo
		if editar_fotoperfil!="":
			cliente.fotoperfil= editar_fotoperfil
		cliente.save()
#Igual que para agencia y fotografo
	elif fotografo!=None:
		editar_NombreUsuario=json['nombreUsuario']
		editar_Descripcion=json['Descripcion']
		editar_numeroTelefono=json['NumeroTelefono']
		editar_usuario=json['usuario']
		editar_correo=json['correo']
		editar_ciudad=json['ciudad']
		editar_fotoperfil=json['fotoPerfil']
		editar_tiktok=json['tiktok']
		editar_instagram= json['instagram']
		editar_twitter= json['facebook']
		if editar_NombreUsuario!="":
			fotografo.nombre = editar_NombreUsuario
		if editar_Descripcion!="":
			fotografo.descripcion = editar_Descripcion
		if editar_numeroTelefono!="":
			fotografo.telefono = editar_numeroTelefono
		if editar_usuario!="":
			fotografo.usuario = editar_usuario
		if editar_correo!="":
			fotografo.email = editar_correo
		if editar_fotoperfil!="":
			fotografo.fotoperfil= editar_fotoperfil
		if editar_tiktok!="":
			fotografo.tiktok=editar_tiktok
		if editar_twitter!="":
			fotografo.twitter=editar_twitter
		if editar_instagram!="":
			fotografo.instagram=editar_twitter
		if editar_ciudad!="":
			fotografo.ciudad=editar_ciudad		
		fotografo.save()
	elif agencia!=None:
		editar_NombreUsuario=json['nombreUsuario']
		editar_Descripcion=json['Descripcion']
		editar_numeroTelefono=json['NumeroTelefono']
		editar_correo=json['correo']
		editar_ciudad=json['ciudad']
		editar_fotoperfil=json['fotoPerfil']
		editar_tiktok=json['tiktok']
		editar_instagram= json['instagram']
		editar_twitter= json['facebook']		
		if editar_NombreUsuario!="":
			agencia.nombre = editar_NombreUsuario
		if editar_Descripcion!="":
			agencia.descripcion = editar_Descripcion
		if editar_numeroTelefono!="":
			agencia.telefono = editar_numeroTelefono
		if editar_correo!="":
			agencia.email = editar_correo
		if editar_fotoperfil!="":
			agencia.fotoperfil= editar_fotoperfil
		if editar_tiktok!="":
			agencia.tiktok=editar_tiktok
		if editar_twitter!="":
			agencia.twitter=editar_twitter
		if editar_instagram!="":
			agencia.instagram=editar_twitter
		if editar_ciudad!="":
			agencia.ciudad=editar_ciudad	
		agencia.save()
"""
def buscar_photograpers(request):

	if request.method == "GET":
	#cogemos los datos del cuerpo
		#json_load=json.loads(request.body)
		query=request.GET.get('query', '')
		#size=json_load['size']
		#rating=json_load['rating']
		#rated_under=json_load['rated_under']
		print(query)

		if query :
			fotografo=Fotografo.objects.filter(
				Q(nombre__icontains=query) 
				| Q(descripcion__icontains=query)
			)
			resultado = []
			i=1
			while i< fotografo.count():
				guardar={}
					
				guardar['id']=fotografo[i].id,
				guardar['Nombre']= fotografo[i].nombre,

				resultado.append(guardar)
				i=i+1
	
			return JsonResponse(resultado, safe=False)
		
		
		if query==None:
			resultado=[]
			resultado=({
				'hola'
			})

			return JsonResponse(resultado)
"""
#realizamos varias sentencias para seleccionar la busqueda correcta
# si query no esta vacio y rating esta vacio realziamos esta busqueda
	if query!="" and rating=="":
			i=1
			#cogemos todos los datos de fotografo quye cumplen con las siguientes sentencias
			fotografo = Fotografo.objects.get(Q(nombre__icontains=query) | Q(descripcion__icontains=query) | Q(ciudad__icontains=query) )
			resultado = []
			#coge ln numero de fotografos que indica el size
			while i< len(fotografo) and i<size:
				resultado= ({
								'id': fotografo[i].id,
								'Nombre': fotografo[i].nombre,
								'FotoPerfil': fotografo[i].fotoperfil,
						}	)
				i=i+1
				media=0
		
# si query no esta vacio y rating no esta vacio realziamos esta busqueda	
	if query!="" and rating!="":
			#cogemos todos los datos de fotografo quye cumplen con las siguientes sentencias
			fotografo = Fotografo.objects.filter(Q(nombre__icontains=query) | Q(descripcion__icontains=query) | Q(ciudad__icontains=query) )
			i=1
			imedia=0
			resultado = []
			#tambien pillamos la media de cada fotografo
			while i< len(fotografo) and imedia<size:
				comentarios = Comentariofotografo.objects.filter(idfotografo=fotografo[i].id)
				for comment in comentarios:
					num_comentarios += 1
					suma_valoracion += Comentariofotografo.valoracion
				media = suma_valoracion / num_comentarios
				#si el rating es el mismo que la media se muestra los siguientes datos
				if rating==media:
					imedia=imedia+1
					resultado.append({
								'id': fotografo[i].id,
								'Nombre': fotografo[i].nombre,
								'FotoPerfil': fotografo[i].fotoperfil,
							}	)
					num_comentarios=0
					suma_valoracion=0
					media=0		
					
					i=i+1
#si query esta vacio y rating no, realiza la siguiente busqueda
	if query=="" and rating!="":
			fotografo = Fotografo.objects.all()
			i=1
			imedia=0
			resultado = []
			while i< len(fotografo) and imedia<size:
				comentarios = Comentariofotografo.objects.filter(idfotografo=fotografo[i].id)
				for comment in comentarios:
					num_comentarios += 1
					suma_valoracion += Comentariofotografo.valoracion
				media = suma_valoracion / num_comentarios
				#si el rating es el mismo que la media se muestra los siguientes datos
				if rating==media:
					imedia=imedia+1
					resultado.append({
								'id': fotografo[i].id,
								'Nombre': fotografo[i].nombre,
								'FotoPerfil': fotografo[i].fotoperfil,
							}	)
					num_comentarios=0
					suma_valoracion=0
					media=0		
					
					i=i+1
#si query esta vacio y rating tambien, realizamos la siguiente busqueda. Selecciona por orden, no tiene filtro
	if query=="" and rating=="":
			fotografo = Fotografo.objects.all()
			i=1
			resultado = []
			while i< len(fotografo) and i<size:
				
				resultado.append({
								'id': fotografo[i].id,
								'Nombre': fotografo[i].nombre,
								'FotoPerfil': fotografo[i].fotoperfil,
	
							}	)
				media=0		
					
				i=i+1			
#El funcionamiento es simialr a la funcion anterior
"""
"""
def buscar_agencies(request):
	
	query=json['query']
	size=json['size']
	rating=json['rating']
	rated_under=json['rated_under']
	if query!="" and rating=="":
			i=1
			agencia = Agencia.objects.get(Q(nombre__icontains=query) | Q(descripcion__icontains=query) | Q(ciudad__icontains=query) )
			resultado = []
			while i< len(agencia) and i<size:
				
				resultado= ({
								'id': agencia[i].id,
								'Nombre': agencia[i].nombre,
			
								'FotoPerfil': agencia[i].fotoperfil,
						}	)
				i=i+1
			
		
	if query!="" and rating!="":
			agencia = Agencias.objects.filter(Q(nombre__icontains=query) | Q(descripcion__icontains=query) | Q(ciudad__icontains=query) )
			i=1
			imedia=0
			resultado = []
			while i< len(agencia) and imedia<size:
				comentarios = Comentarioagencia.objects.filter(idagencia=agencia[i].id)
				for comment in comentarios:
					num_comentarios += 1
					suma_valoracion += Comentarioagencia.valoracion
				media = suma_valoracion / num_comentarios
				if rating==media:
					imedia=imedia+1
					resultado.append({
								'id': agencia[i].id,
								'Nombre': agencia[i].nombre,
							
								'FotoPerfil': agencia[i].fotoperfil,
							}	)
				num_comentarios=0
				suma_valoracion=0
				media=0		
					
				i=i+1
	if query=="" and rating!="":
			agencia = Agencias.objects.all()
			i=1
			imedia=0
			resultado = []
			while i< len(agencia) and imedia<size:
				comentarios = Comentarioagencia.objects.filter(idagencia=agencia[i].id)
				for comment in comentarios:
					num_comentarios += 1
					suma_valoracion += Comentarioagencia.valoracion
				media = suma_valoracion / num_comentarios
				if rating==media:
					imedia=imedia+1
					resultado.append({
								'id': agencia[i].id,
								'Nombre': agencia[i].nombre,
								'FotoPerfil': agencia[i].fotoperfil,
							}	)
				num_comentarios=0
				suma_valoracion=0
				media=0		
					
				i=i+1
	if query=="" and rating=="":
			agencia = Agencias.objects.all()
			i=1
			resultado = []
			while i< len(agencia) and i<size:
				
				resultado.append({
								'id': agencia[i].id,
								'Nombre': agencia[i].nombre,
								'FotoPerfil': agencia[i].fotoperfil,
							}	)
					
				i=i+1			
"""

#Aarón Saavedra Lagares
"""
def photographer (request):
    if request.method == 'GET':
        JsonResponse=[]
        resultado=[]
        id = request.GET['id']
        fotografo = Fotografo()
        fotografo= Fotografo.objects.get(id=id)
        if fotografo==None:
            print('Este fotograf@ no se corresponde con ningun id')
        
        else:
            resultado={
                'id' : fotografo.id,
                'name' : fotografo.name,
                'description' : fotografo.description,
                'phone' : fotografo.phone,
                'instagram' : fotografo.instagram,
                'twitter' : fotografo.twitter,
                'tiktok' : fotografo.tiktok,
                'photo' : fotografo.photo,
                'averageRaiting' : fotografo.averageRaiting
            }
    return JsonResponse (resultado, json_dumps_params={'ensurce_ascii': False})
@csfr_exempt
def agencia (request):
    if request.method == 'GET':
        JsonResponse=[]
        resultado=[]
        id = request.GET['id']
        agencia = Agencia()
        agencia= Agencia.objects.get(id=id)
        if agencia==None:
            print('Este fotograf@ no se corresponde con ningun id')
        
        else:
            resultado={
                'id' : agencia.id,
                'name' : agencia.name,
                'description' : agencia.description,
                'phone' : agencia.phone,
                'instagram' : agencia.instagram,
                'twitter' : agencia.twitter,
                'tiktok' : agencia.tiktok,
                'photo' : agencia.photo,
                'averageRaiting' : agencia.averageRaiting
            }
    return JsonResponse (resultado, json_dumps_params={'ensurce_ascii': False})
@csfr_exempt
# Para utilizar Flask, primero debes instalarlo en tu entorno de desarrollo. Puedes hacerlo utilizando el gestor de paquetes de Python, pip, con el siguiente comando:
# pip install Flask
app = Flask(id)
Comentariofotografo = {
    1: {'comments': [], 'ratings': []},
    2: {'comments': [], 'ratings': []}
}
@app.route('/Comentariofotografo/<int:id>/comments', methods=['POST'])
def add_comment_and_rating(id):
    if id not in Comentariofotografo:
        return jsonify({'message': 'Fotografo no encontrado'}), 404
    if 'SessionToken' not in request.headers:
        return jsonify({'message': 'No estas autorizado'}), 401
    if 'SessionToken' != request.headers['SessionToken']:
        return jsonify({'message': 'No estas autorizado'}), 401
    comment = request.json.get('new_comment')
    rating = request.json.get('new_rating')
    if not comment or not rating:
        return jsonify({'message': 'Bad Request'}), 400
    Comentariofotografo[id]['comentario'].append(comment)
    Comentariofotografo[id]['valoracion'].append(rating)
    return jsonify({'message': 'Comentario y valoración añadidas correctamente'}), 201
if id == '__main__':
    app.run()
@csfr_exempt
app = Flask(id)
Comentarioagencia = {
    1: {'comments': [], 'ratings': []},
    2: {'comments': [], 'ratings': []}
}
@app.route('/Agencia/<int:id>/comments', methods=['POST'])
def add_comment_and_rating(id):
    if id not in Comentarioagencia:
        return jsonify({'message': 'Agencia no encontrado'}), 404
    if 'SessionToken' not in request.headers:
        return jsonify({'message': 'No estas autorizado'}), 401
    if 'SessionToken' != request.headers['SessionToken']:
        return jsonify({'message': 'No estas autorizado'}), 401
    comment = request.json.get('new_comment')
    rating = request.json.get('new_rating')
    if not comment or not rating:
        return jsonify({'message': 'Bad Request'}), 400
    Comentarioagencia[id]['comentario'].append(comment)
    Comentarioagencia[id]['valoracion'].append(rating)
    return jsonify({'message': 'Comentario y valoración añadidas correctamente'}), 201
if id == '__main__':
    app.run()
"""

@csrf_exempt
def register(request):
    if request.method == "POST":
        # Con el try intentamos conseguir el cuerpo de nuestra petición, si no mostraria error 400
        try:
            data = json.loads(request.body)
        except json.decoder.JSONDecodeError:
            return JsonResponse({"message": "Bad request"}, status=400)

        # Con los siguientes if hacemos que si al introducir los datos no llenamos estos campos el valor es nulo
        if not data["surname"]:
            data["surname"] = None

        if not data["username"]:
            data["username"] = None

        if not data["phone"]:
            data["phone"] = None

        if not data["city"]:
            data["city"] = None

        # Si no llenan los campos usuario, email y tipo saltaría el error 400
        if not data["username"] or not data["email"] or not data["type"]:
            return JsonResponse({"message": "Bad request"}, status=400)

        # Comprobariamos si el email coincide en alguno de los registrados en cualquier tipo dentro de la base de datos
        agency_exists = Agencia.objects.filter(
            email=data["email"]
        ).exists()

        client_exists = Clientes.objects.filter(
            email=data["email"]
        ).exists()

        photographer_exists = Fotografo.objects.filter(
            email=data["email"]
        ).exists()

        # Si el email coincide con alguno de nuestra BD, se generaría un conflicto
        if agency_exists or client_exists or photographer_exists:
            return JsonResponse(
                {"message": "User already exists"},
                json_dumps_params={"ensure_ascii": False},
                status=409,
            )

        # Registrar una agencia
        if data["type"] == "agency":
            # Si no se llenan los campos obligatorios saltaría un error 400
            if not data["phone"] or not data["city"]:
                return JsonResponse({"message": "Bad request"}, status=400)
            # Mostraríamos el registro de los datos en Agencia
            agency = Agencia()
            agency.email = data["email"]
            agency.nombre = data["name"]
            agency.contrasena= data["password"]
            agency.telefono= data["phone"]
            agency.ciudad= data["city"]
            agency.save()

        # Registrar un fotografo
        elif data["type"] == "photographer":
            # Si no se llenan los campos obligatorios saltaría un error 400
            if not data["phone"] or not data["city"]:
                return JsonResponse({"message": "Bad request"}, status=400)
            # Mostraríamos el registro de los datos en Fotografo
            photographer = Fotografo()
            photographer.email = data["email"]
            photographer.nombre = data["name"]
            photographer.apellido= data["surname"]
            photographer.contrasena= data["password"]
            photographer.telefono= data["phone"]
            photographer.ciudad= data["city"]
            photographer.save()
        # Registrar un Cliente
        elif data["type"] == "client":
            # Si no se llenan los campos obligatorios saltaría un error 400
            if not data["username"]:
                return JsonResponse({"message": "Bad request"}, status=400)
            # Mostraríamos el registro de los datos en Cliente
            client = Clientes()
            client.email = data["email"]
            client.name = data["name"]
            client.usuario= data["username"]
            client.contrasena = data["password"]
            client.save()

        # Se devuelve un 201 si todo funciona correctamente
        return JsonResponse({"message": "OK"}, status=200)

@csrf_exempt
def sessions(request):
    # Ell método es POST, por lo tanto se creará una nueva sesión
    if request.method == "POST":

        # Buscamos obtener obtener el cuerpo de la petición con try
        try:
            data = json.loads(request.body)
        except json.decoder.JSONDecodeError:
            return JsonResponse({"message": "Bad request"}, status=400)

        # Esto sería una variable
        found = False

        # De la siguiente manera buscamos obtener al usuario de nuestra base de datos con los datos obtenidos
        try:
            user = Agencia.objects.get(email=data["email"])
            found = True
        except ObjectDoesNotExist:
            pass
        
        if found == False:
            try:
                user = Clientes.objects.get(email=data["email"])
                found = True
            except ObjectDoesNotExist:
                pass

        if found == False:
            try:
                user = Fotografo.objects.get(email=data["email"])
                found = True
            except ObjectDoesNotExisst:
                pass

            

        # Procederemos a verificar la contraseña 
        if user.contrasena == data["password"]:
            # Generaremos un token identificativo
            token_string = get_random_string(length=20)
            user.token = token_string
            user.save()

            # Se devolverá un 201 si todo funciona correctamente
            return JsonResponse(
                {"session_token": token_string},
                json_dumps_params={"ensure_ascii": False},
                status=201,
            )
        else:
            # Se devuelve 401 si el usuario no esta autorizado
            return JsonResponse({"message": "Unauthorized"}, status=401)

def search_agency(request):
    if request.method == "GET":
        # Se obtienen los parámetros que indiquemos en la URL
        query = request.GET.get("query", None)
        size = request.GET.get("size", None)
        rating = request.GET.get("rating", 0)

        # Se obtienen los resultados con search
        search = Agencia.objects.filter(nombre__icontains=query).order_by("id")

        # Se almacenarían los datos de cada agencia
        result_list = []
        for agency in search[0 : size]:
            result_list.append({
                "id": agency.id,
                "nombre": agency.nombre,
                "email": agency.email,
                "telefono": agency.telefono,
            })

        # Con este JsonResponse se devolvería una lista
        return JsonResponse(
            result_list,
            json_dumps_params={"ensure_ascii": False},
            safe=False,
            status=200,
        )

@csrf_exempt
def comment_agency(request, agency_id):
    if request.method == "POST":
        # Se busca obtener el cuerpo de la petición
        try:
            data = json.loads(request.body)
        except json.decoder.JSONDecodeError:
            return JsonResponse({"message": "Bad request"}, status=400)

        # Si los datos no existen veríamos un error 400
        if not data["new_comment"] or not data["new_rating"]:
            return JsonResponse({"message": "Bad request"}, status=400)

        # Buscaríamos obtener el SessionToken de los headers
        try:
            session_token = request.headers["SessionToken"]
        except Exception:
            return JsonResponse({"message": "Unauthorized"}, status=401)

        # Se intentaría buscar el cliente de la siguiente manera
        try:
            user = Clientes.objects.get(token=session_token)
        except ObjectDoesNotExist:
            return JsonResponse({"message": "Unauthorized"}, status=401)

        # Se intentaría buscar la Agencia de la siguiente manera
        try:
            agency = Agencia.objects.get(pk=agency_id)
        except ObjectDoesNotExist:
            return JsonResponse({"message": "Not found"}, status=404)

        # Se crea un nuevo comentario
        comment = Comentarioagencia()
        comment.idusuario = user
        comment.idagencia = agency
        comment.comentario = data["new_comment"]
        comment.valoracion = data["new_rating"]
        comment.save()

        # Genera un 200 Ok si el comentario se ha publicado correctamente
        return JsonResponse({"message": "OK"}, status=201)