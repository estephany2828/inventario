from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# categoria = models.ManyToManyField(Categoria, null=True, blank=True)
class Roles (models.Model):
    id_role= models.IntegerField()
    roles = models.CharField(max_length=100)
    def __str__(self):
        return self.roles    
    

class Usuario(models.Model):
    id_cedula = models.IntegerField()
    nombre = models.CharField(max_length=100)
    codigo = models.IntegerField()
    telefono = models.IntegerField()
    rol = models.ForeignKey(Roles, on_delete=models.PROTECT) 
    facultad = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return str(self.id_cedula)

       
class Elemento(models.Model):
    id_elemento = models.IntegerField() 
    encargado = models.CharField(max_length=100)
    facultad = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos',null=True, blank=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return str(self.id_elemento)
   
   
class Sala(models.Model):
    id_Sala= models.IntegerField() 
    numero= models.IntegerField(null=True) 
    piso = models.IntegerField(null=True) 
    encargado = models.CharField(max_length=100, null=True)
    facultad = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return str(self.id_Sala)

class Ip(models.Model):
    id_ip= models.IntegerField() 
    ip_numero =models.IntegerField() 
    mascara = models.IntegerField() 
    asignacion =models.CharField(max_length=100, null=True)
    encargado = models.CharField(max_length=100, null=True)
    facultad = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return str(self.id_ip)
    
  
class Dispositivo (models.Model):
    id_elemento =  models.IntegerField() 
    nombre = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    encargado = models.CharField(max_length=100, null=True)
    facultad = models.CharField(max_length=100, null=True)
    departamento = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return str(self.id_elemento)

class Prestamo (models.Model):
    id_informe = models.IntegerField()
    fecha_inicio= models.DateField(auto_now=False, auto_now_add=False) 
    fecha_fin= models.DateField(auto_now=False, auto_now_add=False) 
    id_pre_sala = models.ForeignKey(Sala, on_delete=models.PROTECT, null=True) 
    id_pre_disp = models.ForeignKey(Dispositivo, on_delete=models.PROTECT, null=True) 
    id_pre_ip = models.ForeignKey(Ip, on_delete=models.PROTECT, null=True)  
    id_pre_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, null=True)  
    status = models.BooleanField(default=True)
    def __str__(self):
        return str(self.id_informe)
 
  
    





    