from django.urls import path
from .views import *
from django.contrib.auth.models import User

urlpatterns = [
    path('inicio_inventario/', login_view, name= 'login'),
    path('contactenos/', contactenos_view, name= 'contactenos'),
    path('principal/', principal_view, name= 'principal'),
    path('register/',  register_view, name="vista_register"), 
    path('quienes_somos/',  quienes_somos_view, name="quienes_somos"), 
  
    #path('estudiantes/',  estudiantes_view, name="estudiantes"), 
    #path('profesores/',  profesores_view, name="profesores"), 
    path('prestamos/',  prestamos_view, name="prestamos"),
    path('informes/',  informes_view, name="informes"), 
    path('perfil/',  perfil_view, name="perfil"), 

    path('lista_sala/', lista_sala_view, name="lista_sala"),
    path('lista_elemento/', lista_elemento_view, name="lista_elemento"),
    path('lista_ip/', lista_ip_view, name="lista_ip"),
    path('lista_usuario/', lista_usuario_view, name="lista_usuario"),

    path('agregar_sala/', agregar_sala_view, name='agregar_sala'),
    path('agregar_ip/', agregar_ip_view, name='agregar_ip'),
    path('agregar_elemento/', agregar_elemento_view, name='agregar_elemento'),
    path('agregar_estudiante/', agregar_estudiante_view, name='agregar_estudiante'),
    path('agregar_profesores/', agregar_profesor_view, name='agregar_profesores'),
    path('agregar_usuario/', agregar_usuario_view, name='agregar_usuario'),

    path('ver_ip/<int:id_ip>/', ver_ip_view, name="ver_ip"),
    path('ver_sala/<int:id_Sala>/', ver_sala_view, name="ver_sala"),
    path('ver_elemento/<int:id_elemento>/', ver_elemento_view, name="ver_elemento"),
    path('ver_usuario/<int:id_cedula>/', ver_usuario_view, name="ver_usuario"),

    path('editar_producto/<int:id_producto>/', editar_producto_view, name="editar_producto"),
    path('editar_sala/<int:id_Sala>/', editar_sala_view, name="editar_sala"),
    path('editar_ip/<int:id_ip>/', editar_ip_view, name="editar_ip"),
    path('editar_elemento/<int:id_elemento>/', editar_elemento_view, name="editar_elemento"),
    path('editar_perfil/<int:id_cedula>/', editar_perfil_view, name="editar_perfil"),
    path('editar_usuario/<int:id_cedula>/', editar_usuario_view, name="editar_usuario"),

    path('eliminar_producto/<int:id_producto>/', eliminar_producto_view, name="eliminar_producto"),
    path('eliminar_sala/<int:id_Sala>/', eliminar_sala_view, name="eliminar_sala"),
    path('eliminar_ip/<int:id_ip>/', eliminar_ip_view, name="eliminar_ip"),
    path('eliminar_elemento/<int:id_elemento>/', eliminar_elemento_view, name="eliminar_elemento"),
     path('eliminar_usuario/<int:id_cedula>/', eliminar_usuario_view, name="eliminar_usuario"),

    path('desactivar_producto/<int:id_producto>/', desactivar_producto_view, name="desactivar_producto"),    
    path('desactivar_sala/<int:id_Sala>/', desactivar_sala_view, name="desactivar_sala"),
    path('desactivar_ip/<int:id_ip>/', desactivar_ip_view, name="desactivar_ip"),
    path('desactivar_elemento/<int:id_elemento>/', desactivar_elemento_view, name="desactivar_elemento"),
    path('desactivar_usuario/<int:id_cedula>/', desactivar_usuario_view, name="desactivar_usuario"),

    path('loginn/', login_view,name='loginn'),
    path('logout/', logout_view,name='logout'),
    
]