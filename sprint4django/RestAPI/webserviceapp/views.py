from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from  .models import Tlibros, Tcomentarios
import json

from .models import Tlibros

def pagina_de_prueba(request):
	return HttpResponse("<h1>Hola Caracola</h1>");

def devolver_libros(request):
	lista = Tlibros.objects.all()
	respuesta_final =[]
	for fila_sql in lista:
		diccionario = {}
		diccionario['id']= fila_sql.id
		diccionario['nombre']= fila_sql.nombre
		diccionario['autor'] =fila_sql.autor
		diccionario['url_imagen'] =fila_sql.url_imagen
		diccionario['genero'] =fila_sql.genero
		respuesta_final.append(diccionario)
	return JsonResponse(respuesta_final, safe=False)

def devolver_libros_por_id(request,id_solicitado):
	libro= Tlibros.objects.get(id=id_solicitado)
	comentarios= libro.tcomentarios_set.all()
	lista_comentarios = []
	for fila_comentario_sql in comentarios:
		diccionario ={}
		diccionario['id']= fila_comentario_sql.id
		diccionario['contraseña']= fila_comentario_sql.contraseña
		diccionario['fecha']= fila_comentario_sql.fecha
		lista_comentarios.append(diccionario)
	resultado= {
		'id': libro.id,
		'nombre': libro.nombre,
		'autor':libro.autor,
		'url_imagen': libro.url_imagen,
		'genero': libro.genero,
		'comentario': lista_comentarios
	}
	return JsonResponse(resultado, json_dumps_params={'ensure_ascii':False})

# Create your views here.
