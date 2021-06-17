from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
# Local imports
from biblioteca.utils.classes.TableConfig import TableConfig
from biblioteca.models import Libro, Autor, Editor
from biblioteca.forms import SearchForm, AutorForm, EditorForm, LibroForm


# Create your views here.
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
        "redirect": "#", # TODO:
    }
    table_conf.update_action = {
        "label":  "Modificar Autor",
        "redirect": "#", # TODO:
    }
    table_conf.delete_action = {
        "label":  "Eliminar Autor",
        "redirect": "#", # TODO:
    }
    # res
    return render(request, "autor_listado.html", {
        "table_config": table_conf,
    })



# def autor_create(request):
#     if request.method == "POST":
#         form = AutorForm(request.POST)

#         if form.is_valid():
#             cd = form.cleaned_data
#             # send_mail(
#             #     cd["asunto"],
#             #     cd["mensaje"],
#             #     cd.get("email", "noreply@example.com"),
#             #     ["fernando.perez.wisphub@gmail.com"]
#             # )
#             print "Autor creado", cd
#             return HttpResponseRedirect("/autores/")
#     else:
#         form = AutorForm(initial={
#             "asunto": "Hola"
#         })
#     return render(request, "autor_update.html", {
#         "form": form,
#         "title": "Crear nuevo Autor",
#         "http_method": "post",
#         "btn_style": "success",
#         "btn_title": "Crear",
#     })



# def autor_update(request, autor_id):
#     print("-->", request.method)
#     if request.method == "POST":
#         form = AutorForm(request.POST)

#         if form.is_valid():
#             cd = form.cleaned_data
#             print "Autor actualizado", cd
#             return HttpResponseRedirect("/autores/")
#     else:
#         form = AutorForm(initial={
#             "nombre": "Hola"
#         })
#     return render(request, "autor_update.html", {
#         "form": form,
#         "title": "Modificar Autor",
#         "http_method": "put",
#         "btn_style": "primary",
#         "btn_title": "Modificar",
#     })


def autor_cu(request, autor_id=None):
    print("-->", request.method)
    if request.method == "POST":
        form = AutorForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            print "Autor actualizado", cd
            return HttpResponseRedirect("/autores/")
    else:
        form = AutorForm(initial={
            "nombre": "Hola"
        })
    return render(request, "autor_update.html", {
        "form": form,
        "title": "Modificar Autor",
        "http_method": "put",
        }.update({
        "btn_style": "primary",
        "btn_title": "Modificar",
    }))





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
        "redirect": "#", # TODO:
    }
    table_conf.update_action = {
        "label":  "Modificar Editor",
        "redirect": "#", # TODO:
    }
    table_conf.delete_action = {
        "label":  "Eliminar Editor",
        "redirect": "#", # TODO:
    }


    
    return render(request, "editor_listado.html", {
        "table_config": table_conf,
    })








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
        "redirect": "#", # TODO:
    }
    table_conf.update_action = {
        "label":  "Modificar Libro",
        "redirect": "#", # TODO:
    }
    table_conf.delete_action = {
        "label":  "Eliminar Libro",
        "redirect": "#", # TODO:
    }


    
    return render(request, "libro_listado.html", {
        "table_config": table_conf,
    })