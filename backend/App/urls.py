from django.urls import path
from . import views 
from .views import LogoutView
 
urlpatterns = [

    path('', views.lobby),

    ############## Path Roles ##############
    path('roles/create', views.crearRol), # Crear nuevo rol
    path('roles/all', views.listaRoles), # Obtener o eliminar todos los roles
    path('roles/<int:pk>', views.encontrarRolId), # Obtener, editar o eliminar un rol dada una id

    ############## Path Usuarios ##############
    path('usuarios/create', views.crearUsuario), # Crear nuevo usuario
    path('usuarios/all', views.listaUsuarios), # Obtener o eliminar todos los usuarios
    path('usuarios/<int:pk>', views.encontrarUsuarioId), # Obtener, editar o eliminar un usuario dada una id

    ############## Path Tecnologias ##############
    path('tecnologias/create', views.crearTecnologia), # Crear nueva tecnologia
    path('tecnologias/all', views.listaTecnologias), # Obtener o eliminar todas las tecnologias
    path('tecnologias/<int:pk>', views.encontrarTecnologiaId), # Obtener, editar o eliminar una tecnologia dada una id

    ############## Path Ejercicios ##############
    path('ejercicios/create', views.crearEjercicio), # Crear nuevo ejercicio
    path('ejercicios/all', views.listaEjercicios), # Obtener o eliminar todos los ejercicios
    path('ejercicios/<int:pk>', views.encontrarEjercicioId), # Obtener, editar o eliminar un ejercicio dada una id

    ############## Path Clases ##############
    path('clases/create', views.crearClase), # Crear nueva clase
    path('clases/all', views.listaClases), # Obtener o eliminar todas las clases
    path('clases/<int:pk>', views.encontrarClaseId), # Obtener, editar o eliminar una clase dada una id

    ############## Path Usuario_Ejercicio ##############
    path('usuario_ejercicio/create', views.crearUsuario_ejercicio), # Crear nuevo usuario_ejercicio
    path('usuario_ejercicio/all', views.listaUsuario_ejercicio), # Obtener o eliminar todos los usuario_ejercicio
    path('usuario_ejercicio/<int:pk>', views.encontrarUsuario_ejercicioId), # Obtener, editar o eliminar un usuario_ejercicio dada una id

    ############## Path Usuario_Clase ##############
    path('usuario_clase/create', views.crearUsuario_clase), # Crear nuevo usuario_clase
    path('usuario_clase/all', views.listaUsuario_clase), # Obtener o eliminar todos los usuario_clase
    path('usuario_clase/<int:pk>', views.encontrarUsuario_ClaseId), # Obtener, editar o eliminar un usuario_clase dada una id

    ############## Path Personalizados ##############
    path('usuarios/passwordless/<int:pk', views.encontrar_usuario_passwordless), # Encontrar usuario sin contrasena
    path('usuarios/cambiarPassword/<int:pk>', views.encontrar_usuario_just_pwd), # Encontrar usuario con constrasena
    path('login', views.login_usuario), # Inicia sesion del usuario dentro de la plataforma
    path('user', views.encontrar_usuario), # Encuenta a un usuario dentro de la plataforma
    path('logout', LogoutView.as_view()), # Cierra sesion del usuario dentro de la plataforma
    path('estudiantes', views.listar_estudiantes), # Lista a todos los estudiantes dentro de la plataforma
    path('ejercicio_usuario/<int:pk>', views.listar_usuario_ejercicio_usuario), # Lista todos los usuario_ejercicio de un usuario por id de usuario
    path('clase_usuario/<int:pk>', views.listar_usuario_clase_usuario), # Lista todos los usuario_clase de un usuario por id de usuario
    path('contar_alumnos', views.contar_alumnos), # Cuenta la cantidad de estudiantes que hay en la plataforma
    path('contar_ejercicios', views.contar_ejercicios), # Cuenta la cantidad de ejercicios que hay en la plataforma
    path('contar_clases', views.contar_clases), # Cuenta la cantidad de clases que hay en la plataforma
    path('contar_ejercicios_resueltos/<int:pk>', views.contar_ejercicios_resueltos), # Cuenta los ejercicios resueltos por un estudiante
    path('contar_clases_completadas/<int:pk>', views.contar_clases_completadas), # Cuenta las clases completadas por un estudiante
    path('sumar_tiempo_ejercicios/<int:pk>', views.sumar_tiempo_ejercicios), # Suma el tiempo total que un estudiante demoro en resolver todos los ejercicios
    path('sumar_tiempo_clases/<int:pk>', views.sumar_tiempo_clases), # Suma el tiempo total que el estudiante paso completando todas las clases
    path('listar_clases_usuario_tecnologia/<int:pk1>/<int:pk2>', views.listar_clases_usuario_tecnologia), # Lista todos los usuario_clase dada una id de tecnologia y una id de usuario
    path('listar_ejercicios_usuario_tecnologia/<int:pk1>/<int:pk2>', views.listar_ejercicios_usuario_tecnologia), # Lista todos los usuario_ejercicio dada una id de tecnologia y una id de usuario con estado 0
]