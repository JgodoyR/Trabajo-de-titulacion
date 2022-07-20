from django.shortcuts import render

from django.http.response import JsonResponse
from django.db.models import Count, Sum
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.contrib.auth.hashers import make_password

import App.models as models
import App.serializers as serials
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
import jwt, datetime
from django.contrib.auth.models import update_last_login

# Create your views here.

def lobby(request):
    return render(request, 'lobby.html')

############## CRUD Roles ##############

# Crear un rol
@api_view(['POST'])
def crearRol(request):
    rolData = JSONParser().parse(request)
    rolesSerializer = serials.RolesSerializer(data=rolData)
    if rolesSerializer.is_valid():
        rolesSerializer.save()
        return JsonResponse(rolesSerializer.data, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse(rolesSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Obtener o eliminar todos los roles
@api_view(['GET', 'DELETE'])
def listaRoles(request):
    if request.method == 'GET':
        roles = models.Roles.objects.all()
        rolesSerializer = serials.RolesSerializer(roles, many=True)
        return JsonResponse(rolesSerializer.data, safe=False)

    elif request.method == 'DELETE':
        count = models.Roles.objects.all().delete()
        return JsonResponse({'message': 'Se borraron exitosamente {} todos los roles.'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

# Obtener, modificar o eliminar un rol dada una id
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def encontrarRolId(request, pk):
    rol = models.Roles.objects.get(pk=pk)

    if request.method == 'GET':
        rolesSerializer = serials.RolesSerializer(rol)
        return JsonResponse(rolesSerializer.data)

    elif request.method in ['PUT', 'PATCH']:
        rolData = JSONParser().parse(request)
        rolesSerializer = serials.RolesSerializer(rol, data=rolData)
        if rolesSerializer.is_valid():
            rolesSerializer.save()
            return JsonResponse(rolesSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(rolesSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        rol.delete()
        return JsonResponse({'message': 'El rol fue eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)

############## CRUD Usuarios ##############

# Crear un usuario
@api_view(['POST'])
def crearUsuario(request):
    usuarioData = JSONParser().parse(request)
    usuariosSerializer = serials.UsuariosSerializer(data=usuarioData)
    if usuariosSerializer.is_valid():
        usuariosSerializer.save()
        return JsonResponse(usuariosSerializer.data, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse(usuariosSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Obtener o eliminar todos los usuarios
@api_view(['GET', 'DELETE'])
def listaUsuarios(request):
    if request.method == 'GET':
        usuarios = models.Usuarios.objects.all()
        usuariosSerializer = serials.UsuariosSerializer(usuarios, many=True)
        return JsonResponse(usuariosSerializer.data, safe=False)

    elif request.method == 'DELETE':
        count = models.Usuarios.objects.all().delete()
        return JsonResponse({'message': 'Se borraron exitosamente {} usuarios.'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)

# Obtener, modificar o eliminar un usuario dada una id
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def encontrarUsuarioId(request, pk):
    usuario = models.Usuarios.objects.get(pk=pk)

    if request.method == 'GET':
        usuariosSerializer = serials.UsuariosSerializer(usuario)
        return JsonResponse(usuariosSerializer.data)

    elif request.method in ['PUT', 'PATCH']:
        usuarioData = JSONParser().parse(request)
        usuariosSerializer = serials.UsuariosSerializer(usuario, data=usuarioData)
        if usuariosSerializer.is_valid():
            usuariosSerializer.save()
            return JsonResponse(usuariosSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(usuariosSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        usuario.delete()
        return JsonResponse({'message': 'El usuario fue eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)

############## CRUD Tecnologias ##############

# Crear una tecnologia
@api_view(['POST'])
def crearTecnologia(request):
    tecnologiaData = JSONParser().parse(request)
    tecnologiasSerializer = serials.TecnologiasSerializer(data=tecnologiaData)
    if tecnologiasSerializer.is_valid():
        tecnologiasSerializer.save()
        return JsonResponse(tecnologiasSerializer.data, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse(tecnologiasSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Obtener o eliminar todas las tecnologias
@api_view(['GET', 'DELETE'])
def listaTecnologias(request):
    if request.method == 'GET':
        tecnologias = models.Tecnologias.objects.all()
        tecnologiasSerializer = serials.TecnologiasSerializer(tecnologias, many=True)
        return JsonResponse(tecnologiasSerializer.data, safe=False)

    elif request.method == 'DELETE':
        count = models.Tecnologias.objects.all().delete()
        return JsonResponse({'message': 'Se borraron exitosamente {} tecnologias.'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)

# Obtener, modificar o eliminar una tecnologia dada una id
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def encontrarTecnologiaId(request, pk):
    tecnologia = models.Tecnologias.objects.get(pk=pk)

    if request.method == 'GET':
        tecnologiasSerializer = serials.TecnologiasSerializer(tecnologia)
        return JsonResponse(tecnologiasSerializer.data)

    elif request.method in ['PUT', 'PATCH']:
        tecnologiaData = JSONParser().parse(request)
        tecnologiasSerializer = serials.TecnologiasSerializer(tecnologia, data=tecnologiaData)
        if tecnologiasSerializer.is_valid():
            tecnologiasSerializer.save()
            return JsonResponse(tecnologiasSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(tecnologiasSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tecnologia.delete()
        return JsonResponse({'message': 'La tecnologia fue eliminada correctamente'}, status=status.HTTP_204_NO_CONTENT)

############## CRUD Ejercicios ##############

# Crear un ejercicio
@api_view(['POST'])
def crearEjercicio(request):
    ejercicioData = JSONParser().parse(request)
    ejerciciosSerializer = serials.EjerciciosSerializer(data=ejercicioData)
    if ejerciciosSerializer.is_valid():
        ejerciciosSerializer.save()
        return JsonResponse(ejerciciosSerializer.data, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse(ejerciciosSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Obtener o eliminar todos los ejercicios
@api_view(['GET', 'DELETE'])
def listaEjercicios(request):
    if request.method == 'GET':
        ejercicios = models.Ejercicios.objects.all()
        ejerciciosSerializer = serials.EjerciciosSerializer(ejercicios, many=True)
        return JsonResponse(ejerciciosSerializer.data, safe=False)

    elif request.method == 'DELETE':
        count = models.Ejercicios.objects.all().delete()
        return JsonResponse({'message': 'Se borraron exitosamente {} ejercicios.'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)

# Obtener, modificar o eliminar un ejercicio dada una id
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def encontrarEjercicioId(request, pk):
    ejercicio = models.Ejercicios.objects.get(pk=pk)

    if request.method == 'GET':
        ejerciciosSerializer = serials.EjerciciosSerializer(ejercicio)
        return JsonResponse(ejerciciosSerializer.data)

    elif request.method in ['PUT', 'PATCH']:
        ejercicioData = JSONParser().parse(request)
        ejerciciosSerializer = serials.EjerciciosSerializer(ejercicio, data=ejercicioData)
        if ejerciciosSerializer.is_valid():
            ejerciciosSerializer.save()
            return JsonResponse(ejerciciosSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(ejerciciosSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ejercicio.delete()
        return JsonResponse({'message': 'El ejercicio fue eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)

############## CRUD Clases ##############

# Crear una clase
@api_view(['POST'])
def crearClase(request):
    clasesData = JSONParser().parse(request)
    clasesSerializer = serials.ClasesSerializer(data=clasesData)
    if clasesSerializer.is_valid():
        clasesSerializer.save()
        return JsonResponse(clasesSerializer.data, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse(clasesSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Obtener o eliminar todas las clases
@api_view(['GET', 'DELETE'])
def listaClases(request):
    if request.method == 'GET':
        clases = models.Clases.objects.all()
        clasesSerializer = serials.ClasesSerializer(clases, many=True)
        return JsonResponse(clasesSerializer.data, safe=False)

    elif request.method == 'DELETE':
        count = models.Clases.objects.all().delete()
        return JsonResponse({'message': 'Se borraron exitosamente {} clases.'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)

# Obtener, modificar o eliminar una clase dada una id
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def encontrarClaseId(request, pk):
    clase = models.Clases.objects.get(pk=pk)

    if request.method == 'GET':
        clasesSerializer = serials.ClasesSerializer(clase)
        return JsonResponse(clasesSerializer.data)

    elif request.method in ['PUT', 'PATCH']:
        claseData = JSONParser().parse(request)
        clasesSerializer = serials.ClasesSerializer(clase, data=claseData)
        if clasesSerializer.is_valid():
            clasesSerializer.save()
            return JsonResponse(clasesSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(clasesSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        clase.delete()
        return JsonResponse({'message': 'La clase fue eliminada correctamente'}, status=status.HTTP_204_NO_CONTENT)

############## CRUD Usuario_Ejercicio ##############

# Crear un usuario_ejercicio
@api_view(['POST'])
def crearUsuario_ejercicio(request):
    usuario_ejercicioData = JSONParser().parse(request)
    usuario_ejercicioSerializer = serials.Usuario_EjercicioSerializer(data=usuario_ejercicioData)
    if usuario_ejercicioSerializer.is_valid():
        usuario_ejercicioSerializer.save()
        return JsonResponse(usuario_ejercicioSerializer.data, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse(usuario_ejercicioSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Obtener o eliminar todos los usuario_ejercicio
@api_view(['GET', 'DELETE'])
def listaUsuario_ejercicio(request):
    if request.method == 'GET':
        usuario_ejercicio = models.Usuario_Ejercicio.objects.all()
        usuario_ejercicioSerializer = serials.Usuario_EjercicioSerializer(usuario_ejercicio, many=True)
        return JsonResponse(usuario_ejercicioSerializer.data, safe=False)

    elif request.method == 'DELETE':
        count = models.Usuario_Ejercicio.objects.all().delete()
        return JsonResponse({'message': 'Se borraron exitosamente {} usuario_ejercicio.'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)

# Obtener, modificar o eliminar un usuario_ejercicio dada una id
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def encontrarUsuario_ejercicioId(request, pk):
    usuario_ejercicio = models.Usuario_Ejercicio.objects.get(pk=pk)

    if request.method == 'GET':
        usuario_ejercicioSerializer = serials.Usuario_EjercicioSerializer(usuario_ejercicio)
        return JsonResponse(usuario_ejercicioSerializer.data)

    elif request.method in ['PUT', 'PATCH']:
        usuario_ejercicioData = JSONParser().parse(request)
        usuario_ejercicioSerializer = serials.Usuario_EjercicioSerializer(usuario_ejercicio, data=usuario_ejercicioData)
        if usuario_ejercicioSerializer.is_valid():
            usuario_ejercicioSerializer.save()
            return JsonResponse(usuario_ejercicioSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(usuario_ejercicioSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        usuario_ejercicio.delete()
        return JsonResponse({'message': 'El usuario_ejercicio fue eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)

############## CRUD Usuario_Clase ##############

# Crear un usuario_clase
@api_view(['POST'])
def crearUsuario_clase(request):
    usuario_claseData = JSONParser().parse(request)
    usuario_claseSerializer = serials.Usuario_ClaseSerializer(data=usuario_claseData)
    if usuario_claseSerializer.is_valid():
        usuario_claseSerializer.save()
        return JsonResponse(usuario_claseSerializer.data, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse(usuario_claseSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Obtener o eliminar todos los usuario_clase
@api_view(['GET', 'DELETE'])
def listaUsuario_clase(request):
    if request.method == 'GET':
        usuario_clase = models.Usuario_Clase.objects.all()
        usuario_claseSerializer = serials.Usuario_ClaseSerializer(usuario_clase, many=True)
        return JsonResponse(usuario_claseSerializer.data, safe=False)

    elif request.method == 'DELETE':
        count = models.Usuario_Clase.objects.all().delete()
        return JsonResponse({'message': 'Se borraron exitosamente {} usuario_clase.'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)

# Obtener, modificar o eliminar un usuario_clase dada una id
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def encontrarUsuario_ClaseId(request, pk):
    usuario_clase = models.Usuario_Clase.objects.get(pk=pk)

    if request.method == 'GET':
        usuario_claseSerializer = serials.Usuario_ClaseSerializer(usuario_clase)
        return JsonResponse(usuario_claseSerializer.data)

    elif request.method in ['PUT', 'PATCH']:
        usuario_claseData = JSONParser().parse(request)
        usuario_claseSerializer = serials.Usuario_ClaseSerializer(usuario_clase, data=usuario_claseData)
        if usuario_claseSerializer.is_valid():
            usuario_claseSerializer.save()
            return JsonResponse(usuario_claseSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(usuario_claseSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        usuario_clase.delete()
        return JsonResponse({'message': 'El usuario_clase fue eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)

############## Personalizadas ##############

# Encontrar usuario logeado
@api_view(['POST'])
def encontrar_usuario(request):
    tok = JSONParser().parse(request)
    token = tok['jwt']

    response = Response()

    if not token:
        response.data = {
        'message': 'success'
    }

    try:
        payload = jwt.decode(token, 'secret', algorithms='HS256')
    except jwt.ExpiredSignatureError:
        response.data = {
        'message': 'success'
    }

    user = models.Usuarios.objects.get(id=payload['id'])
    serializer = serials.UsuariosSerializer(user)

    return Response(serializer.data)

# Login
@api_view(['POST'])
def login_usuario(request):
    tok = JSONParser().parse(request)
    rut = tok['rut']
    password = tok['password']

    user = models.Usuarios.objects.filter(rut=rut).first()
    if user is None:
        return JsonResponse({'message': 'No existe el usuario'}, status=status.HTTP_400_BAD_REQUEST)
    if not user.check_password(password):
        return JsonResponse({'message': 'Contrasena incorrecta'}, status=status.HTTP_400_BAD_REQUEST)
    payload = {
        'id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
    }

    token = jwt.encode(payload, 'secret', algorithm='HS256')

    response = Response()
    
    response.data ={
        'jwt': token,
        'last_login': update_last_login(None, user)
    }
    return response

# Logout
class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response

# Encontrar usuario sin contrasena
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def encontrar_usuario_passwordless(request, pk):
    usuario = models.Usuarios.objects.get(pk=pk)

    if request.method == 'GET':
        usuariosSerializer = serials.UsuariosPasswordlessSerializer(usuario)
        return JsonResponse(usuariosSerializer.data)

    elif request.method in ['PUT', 'PATCH']:
        usuarioData = JSONParser().parse(request)
        usuariosSerializer = serials.UsuariosPasswordlessSerializer(usuario, data=usuarioData)
        if usuariosSerializer.is_valid():
            usuariosSerializer.save()
            return JsonResponse(usuariosSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(usuariosSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        usuario.delete()
        return JsonResponse({'message': 'El usuario fue correctamente eliminado'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def encontrar_usuario_just_pwd(request, pk):
    usuario = models.Usuarios.objects.get(pk=pk)

    if request.method == 'GET':
        usuariosSerializer = serials.UsuariosPasswordSerializer(usuario)
        return JsonResponse(usuariosSerializer.data)

    elif request.method in ['PUT', 'PATCH']:
        usuarioData = JSONParser().parse(request)
        pwd = usuarioData['old_password']
        check = usuario.check_password(pwd)
        
        usuarioData['password'] = make_password(usuarioData['password'])
        usuariosSerializer = serials.UsuariosPasswordSerializer(usuario, data=usuarioData)

        if not check:
            return JsonResponse({'message': 'La clave actual ingresada no coincide.'},
                status=status.HTTP_201_CREATED)

        if usuariosSerializer.is_valid():
            usuariosSerializer.save()
            return JsonResponse({'message': 'La clave se ha modificado con exito.'}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(usuariosSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Listar estudiantes
@api_view(['GET'])
def listar_estudiantes(request):
    usuarios = models.Usuarios.objects.filter(rol=3)
    usuariosSerializer = serials.UsuariosSerializer(usuarios, many=True)
    return JsonResponse(usuariosSerializer.data, safe=False)

#Listar todos los usuario_ejercicio de un usuario por id de usuario
@api_view(['GET'])
def listar_usuario_ejercicio_usuario(request, pk):
    ejercicio_usuario = models.Usuario_Ejercicio.objects.filter(usuario=pk)
    ejercicio_usuarioSerializer = serials.Usuario_EjercicioCruzSerializer(ejercicio_usuario, many=True)
    return JsonResponse(ejercicio_usuarioSerializer.data, safe=False)

#Listar todos los usuario_clase de un usuario por id de usuario
@api_view(['GET'])
def listar_usuario_clase_usuario(request, pk):
    clase_usuario = models.Usuario_Clase.objects.filter(usuario=pk)
    clase_usuarioSerializer = serials.Usuario_ClaseCruzSerializer(clase_usuario, many=True)
    return JsonResponse(clase_usuarioSerializer.data, safe=False)

# Contar la cantidad de alumnos
@api_view(['GET'])
def contar_alumnos(request):
    cantidad_alumnos = models.Usuarios.objects.filter(rol='3').annotate(Count('rol')).count()
    return JsonResponse(cantidad_alumnos, safe=False)

# Contar la cantidad de ejercicios
@api_view(['GET'])
def contar_ejercicios(request):
    cantidad_ejercicios = models.Ejercicios.objects.count()
    return JsonResponse(cantidad_ejercicios, safe=False)

# Contar la cantidad de clases
@api_view(['GET'])
def contar_clases(request):
    cantidad_clases = models.Clases.objects.count()
    return JsonResponse(cantidad_clases, safe=False)

# Contar cantidad de ejercicios resueltos
@api_view(['GET'])
def contar_ejercicios_resueltos(request, pk):
    ejercicios_resueltos = models.Usuario_Ejercicio.objects.filter(usuario=pk, estado='1').annotate(Count('estado')).count()
    return JsonResponse(ejercicios_resueltos, safe=False)

# Contar cantidad de clases finalizadas
@api_view(['GET'])
def contar_clases_completadas(request, pk):
    clases_completadas = models.Usuario_Clase.objects.filter(usuario=pk, estado='1').annotate(Count('estado')).count()
    return JsonResponse(clases_completadas, safe=False)

# Sumar cantidad de tiempo ejercicios
@api_view(['GET'])
def sumar_tiempo_ejercicios(request, pk):
    tiempo_ejercicios = models.Usuario_Ejercicio.objects.filter(usuario=pk).aggregate(Sum('tiempo')).get('tiempo__sum')
    return JsonResponse(tiempo_ejercicios, safe=False)

# Sumar cantidad de tiempo clases
@api_view(['GET'])
def sumar_tiempo_clases(request, pk):
    tiempo_clases = models.Usuario_Clase.objects.filter(usuario=pk).aggregate(Sum('tiempo')).get('tiempo__sum')
    return JsonResponse(tiempo_clases, safe=False)

# Listar todas las clases dada una id de usuario y una id de tecnologia
@api_view(['GET'])
def listar_clases_usuario_tecnologia(request, pk1, pk2):
    
    clases = models.Clases.objects.filter(tecnologia=pk1)
    claseSerializer = serials.ClasesCruzSerializer(clases, many=True)

    claseIds = []
    for clase in claseSerializer.data:
        claseIds.append(clase['id'])

    usuario_clase = models.Usuario_Clase.objects.filter(clase__in=claseIds, usuario=pk2)
    usuario_claseSerializer = serials.Usuario_ClaseCruzSerializer(usuario_clase, many=True)
    return JsonResponse(usuario_claseSerializer.data, safe=False)

# Listar todos los ejercicios dada una id de usuario y una id de tecnologia
@api_view(['GET'])
def listar_ejercicios_usuario_tecnologia(request, pk1, pk2):
    
    ejercicios = models.Ejercicios.objects.filter(tecnologia=pk1)
    ejercicioSerializer = serials.EjercicioCruzSerializer(ejercicios, many=True)

    ejercicioIds = []
    for ejercicio in ejercicioSerializer.data:
        ejercicioIds.append(ejercicio['id'])

    usuario_ejercicio = models.Usuario_Ejercicio.objects.filter(ejercicio__in=ejercicioIds, usuario=pk2, estado='0')
    usuario_ejercicioSerializer = serials.Usuario_EjercicioCruzSerializer(usuario_ejercicio, many=True)
    return JsonResponse(usuario_ejercicioSerializer.data, safe=False)