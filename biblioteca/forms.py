from django import forms

class SearchForm(forms.Form):
    """
    """
    q = forms.CharField(label="Buscador", max_length=50, required=False)
    
    
    
class AutorForm(forms.Form):
    nombre = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        "id": "name",
        "class": "form-control",
    }))
    apellidos = forms.CharField(max_length=40, widget=forms.TextInput(attrs={
        "id": "apellidos",
        "class": "form-control",
    }))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={
        "id": "email",
        "class": "form-control",
    }))
    


class EditorForm(forms.Form):
    nombre  = forms.CharField(max_length=30)
    domicilio = forms.CharField(max_length=50)
    ciudad = forms.CharField(max_length=60)
    estado = forms.CharField(max_length=30)
    pais = forms.CharField(max_length=50)
    website = forms.URLField(required=False)
    

class LibroForm(forms.Form):
    titulo = forms.CharField(max_length=100)
    # autores = forms.ManyToManyField(Autor)
    # editor = forms.ForeignKey(Editor)
    fecha_publicacion = forms.DateField(required=False)
    portada = forms.ImageField(required=False)
    