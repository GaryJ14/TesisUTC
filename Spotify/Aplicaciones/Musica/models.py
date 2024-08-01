from django.db import models

# Create your models here.
class Registro(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    confirmPassword= models.CharField(max_length=255)

    def __str__(self):
        fila = "{0}: {1} - {2} - {3} - {4}"
        return fila.format(self.id, self.nombre, self.email, self.password, self.confirmPassword)
#class Cuenta(models.Model):
    #id = models.AutoField(primary_key=True)
    #usuarioId = models.IntegerField()  # Este campo puede ser una clave foránea a otro modelo de usuario si es necesario
    #fechaCreacion = models.DateTimeField(default=timezone.now)
    #estado = models.CharField(max_length=10, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default='activo')

    #def __str__(self):
     #   fila = "{0}: Usuario ID {1} - Estado: {2}
      #  return fila.format(self.cuentaId, self.usuarioId, self.estado)
    