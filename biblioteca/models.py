from django.db import models

# Create your models here.
class Editor(models.Model):
    nombre  = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=60)
    estado = models.CharField(max_length=30)
    pais = models.CharField(max_length=50)
    website = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ["nombre"]
        verbose_name = 'Editor'
        verbose_name_plural = "Editores"
    
    def __str__(self):
        return ("Editor<"
            + "nombre='{}'"
            + ", domicilio='{}'"
            + ", ciudad='{}'"
            + ", estado='{}'"
            + ", pais='{}'"
            + ", website='{}'"
            + ">"
        ).format(
            self.nombre,
            self.domicilio,
            self.ciudad,
            self.estado,
            self.pais,
            self.website
        ) 
    


class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=40)
    email = models.EmailField(null=True, blank=True)

    class Meta:
        ordering = ["-apellidos", "-nombre"]
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def get_field(self, field):
        return self[field]
    
    def __str__(self):
        return ("Autor<nombre='{}', apellidos='{}'>").format(self.nombre,self.apellidos,)
    


class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor)
    editor = models.ForeignKey(Editor)
    fecha_publicacion = models.DateField(null=True, blank=True)
    portada = models.ImageField(upload_to="portadas", null=True, blank=True)

    class Meta:
        ordering = ["-fecha_publicacion", "-titulo"]
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return "Libro<titulo={}>".format(self.titulo)
