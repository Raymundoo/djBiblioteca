from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q
# Local imports
from biblioteca.utils.classes.TableConfig import TableConfig
from biblioteca.models import Libro, Autor, Editor
from biblioteca.forms import SearchForm, AutorForm, EditorForm, LibroForm


#region utils
def cu_response(request, form, key, is_new):
    """
    Elabora la respuesta para el template de crear/actualizar
    """
    return render(request, "{}_cu.html".format(key), {
        "form":         form,
        "title":        "{} {}".format("Modificar" if is_new else "Crear", key.capitalize()),
        "btn_title":    "Modificar" if is_new else "Crear",
    })



def delete_response(request, entity, redirect):
    """
    Elimina una entidad mediante el id enviado como "dlt_id" desde el post
    """
    if request.method == "POST" and "dlt_id" in request.POST:
        autor = entity.objects.get(id=request.POST["dlt_id"])
        autor.delete()
    return HttpResponseRedirect(redirect)
#endregion




#region autor views
def autor_listado(request):
    table_conf = TableConfig()
    form = SearchForm(request.GET)
    table_conf.form = form

    # filter
    if form.is_valid():
        cd = form.cleaned_data
        if not cd['q']:
            table_conf.datasource = Autor.objects.all().values()
        else:
            table_conf.datasource = Autor.objects.filter(
                Q(nombre__icontains=cd['q'])    |
                Q(apellidos__icontains=cd['q']) |
                Q(email__icontains=cd['q'])
            ).values()

    # table config
    table_conf.fields = [
        { "label": "Nombre",    "key": "nombre" },
        { "label": "Apellidos", "key": "apellidos" },
        { "label": "Email",     "key": "email" },
    ]
    table_conf.create_action = {
        "label":  "Crear nuevo Autor",
        "redirect": "crear/autor",
    }
    table_conf.update_action = {
        "label":  "Modificar Autor",
        "redirect": "modificar/autor",
    }
    table_conf.delete_action = {
        "label":  "Eliminar Autor",
        "redirect": "eliminar/autor",
    }
    # res
    return render(request, "autor_listado.html", {
        "table_config": table_conf,
    })



def autor_cu(request, autor_id=None):
    form = None

    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # Agregar nuevo autor
            if not autor_id:
                Autor.objects.create(**cd)
            # Actualizar autor
            else:
                Autor.objects.filter(id=autor_id).update(**cd)
            return HttpResponseRedirect("/autores")

    else:
        # Inicializar el form con valores actuales del usuario
        if autor_id:
            try:
                autor = Autor.objects.get(id=autor_id)
                form = AutorForm(initial={
                    "nombre": autor.nombre,
                    "apellidos": autor.apellidos,
                    "email": autor.email,
                })
            except Autor.DoesNotExist:
                return HttpResponseRedirect("/autores")
        
        # Inicializar form vacio para nuevo usuario
        else:
            form = AutorForm()

    return cu_response(request, form, "autor", bool(autor_id))


def autor_delete(request):
    return delete_response(request, Autor, "/autores")
#endregion




#region Editor views
def editor_listado(request):
    table_conf = TableConfig()
    form = SearchForm(request.GET)
    table_conf.form = form

    # filter
    if form.is_valid():
        cd = form.cleaned_data
        if not cd['q']:
            table_conf.datasource = Editor.objects.all().values()
        else:
            table_conf.datasource = Editor.objects.filter(
                Q(nombre__icontains=cd['q']) |
                Q(ciudad__icontains=cd['q']) |
                Q(estado__icontains=cd['q']) |
                Q(pais__icontains=cd['q'])
            ).values()
    

    table_conf.fields = [
        { "label": "Nombre",        "key": "nombre" },
        { "label": "Domicilio",     "key": "domicilio" },
        { "label": "Ciudad",        "key": "ciudad" },
        { "label": "Estado",        "key": "estado" },
        { "label": "Pais",          "key": "pais" },
        { "label": "Sitio oficial", "key": "website", "is_link":True },
    ]
    table_conf.create_action = {
        "label":  "Crear nuevo Editor",
        "redirect": "crear/editor",
    }
    table_conf.update_action = {
        "label":  "Modificar Editor",
        "redirect": "modificar/editor",
    }
    table_conf.delete_action = {
        "label":  "Eliminar Editor",
        "redirect": "eliminar/editor",
    }


    
    return render(request, "editor_listado.html", {
        "table_config": table_conf,
    })



def editor_cu(request, editor_id=None):
    form = None

    if request.method == "POST":
        form = EditorForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # Agregar nuevo editor
            if not editor_id:
                autor = Editor.objects.create(**cd)
            # Actualizar editor
            else:
                autor = Editor.objects.filter(id=editor_id).update(**cd)
            return HttpResponseRedirect("/editores")

    else:
        # Inicializar el form con valores actuales del usuario
        if editor_id:
            try:
                editor = Editor.objects.get(id=editor_id)
                form = EditorForm(initial={
                    "nombre":    editor.nombre,
                    "domicilio": editor.domicilio,
                    "ciudad":    editor.ciudad,
                    "estado":    editor.estado,
                    "pais":      editor.pais,
                    "website":   editor.website,
                })
            except Editor.DoesNotExist:
                return HttpResponseRedirect("/editores")
        
        # Inicializar form vacio para nuevo usuario
        else:
            form = EditorForm()
    
    return cu_response(request, form, "editor", bool(editor_id))



def editor_delete(request):
    return delete_response(request, Editor, "/editores")
#endregion




#region Libro views
def libro_listado(request):
    table_conf = TableConfig()
    form = SearchForm(request.GET)
    table_conf.form = form

    # filter
    if form.is_valid():
        cd = form.cleaned_data
        if not cd['q']:
            table_conf.datasource = Libro.objects.all().values()
        else:
            table_conf.datasource = Libro.objects.filter(
                titulo__icontains=cd['q']
            ).values()

    table_conf.fields = [
        { "label": "Portada",               "key": "portada" },
        { "label": "Titulo",                "key": "titulo" },
        { "label": "Autores",               "key": "autores" },
        { "label": "Fecha de publicacion",  "key": "fecha_publicacion" },
        { "label": "Editor",                "key": "editor" },
    ]
    table_conf.create_action = {
        "label":  "Dar de alta libro",
        "redirect": "crear/autor",
    }
    table_conf.update_action = {
        "label":  "Modificar Libro",
        "redirect": "modificar/autor",
    }
    table_conf.delete_action = {
        "label":  "Eliminar Libro",
        "redirect": "eliminar/libro",
    }


    
    return render(request, "libro_listado.html", {
        "table_config": table_conf,
    })



def libro_delete(request):
    return delete_response(request, Libro, "/libros")
#endregion