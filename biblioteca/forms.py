from django import forms

#region utilds
def build_attrs(key):
    return {
        "id":               key,
        "aria-describedby": "{}_errors".format(key),
        "class":            "form-control",
    }
#endregion



class SearchForm(forms.Form):
    q = forms.CharField(label="Buscador", max_length=50, required=False)
    
    
    
class AutorForm(forms.Form):
    nombre = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs=build_attrs("nombre"))
    )
    apellidos = forms.CharField(
        max_length=40,
        widget=forms.TextInput(attrs=build_attrs("apellidos"))
    )
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs=build_attrs("email"))
    )
    


class EditorForm(forms.Form):
    nombre = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs=build_attrs("nombre"))
    )
    domicilio = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs=build_attrs("domicilio"))
    )
    ciudad = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs=build_attrs("ciudad"))
    )
    estado = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs=build_attrs("estado"))
    )
    pais = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs=build_attrs("pais"))
    )
    website = forms.URLField(
        required=False,
        widget=forms.TextInput(attrs=build_attrs("website"))
    )



class LibroForm(forms.Form):
    titulo = forms.CharField(max_length=100)
    # autores = forms.ManyToManyField(Autor)
    # editor = forms.ForeignKey(Editor)
    fecha_publicacion = forms.DateField(required=False)
    portada = forms.ImageField(required=False)
    