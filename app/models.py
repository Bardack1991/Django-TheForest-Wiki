from django.db import models

#modelo usuario

class Usuario(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre de usuario')
    email = models.EmailField(max_length=50, unique=True, verbose_name='Correo electrónico')
    password = models.CharField(max_length=255, verbose_name='Contraseña')
    
    def __str__(self):
        return self.nombre