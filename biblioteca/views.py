from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
# Local imports
from biblioteca.models import Libro, Autor, Editor
from biblioteca.forms import SearchForm, AutorForm, EditorForm, LibroForm


#region utils
def generic_delete(request, instance, tpl_name, redirect):
    if request.method == "POST":
        instance.delete()
        return HttpResponseRedirect( redirect )
    return render(request, tpl_name, { "object": instance })
#endregion




#region autor views
def autor_listado(request):
    form, datasource = SearchForm(request.GET), []

    # filter
    if form.is_valid():
        cd = form.cleaned_data
        if not cd['q']:
            datasource = Autor.objects.all().values()
        else:
            datasource = Autor.objects.filter(
                Q(nombre__icontains=cd['q'])    |
                Q(apellidos__icontains=cd['q']) |
                Q(email__icontains=cd['q'])
            ).values()
    return render(request, "autor_listado.html", {
        "buscador": form,
        "object_list": datasource,
        "fields": [
            { "label": "Nombre",    "key": "nombre" },
            { "label": "Apellidos", "key": "apellidos" },
            { "label": "Email",     "key": "email" },
        ],
        "actions": {
            "create": { "label": "Crear Autor", "redirect": "/crear/autor" },
            "update": { "label": "Modificar",   "redirect": "/modificar/autor" },
            "delete": { "label": "Eliminar",    "redirect": "/eliminar/autor" },
        }
    })



def autor_form(request, autor_id=None):
    # Se verifica la existencia
    autor_instance = get_object_or_404(Autor, id=autor_id) if autor_id else None
    # Update/create
    if request.method == "POST":
        form = AutorForm(request.POST, instance=autor_instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/autores")
    else:
        form = AutorForm(instance=autor_instance) if autor_instance else AutorForm()
    return render(request, "autor_form.html", {
        "form":   form,
        "action": "Modificar" if autor_instance else "Crear",
    })



def autor_delete(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    return generic_delete(
        request=request,
        instance=autor,
        tpl_name="autor_delete.html",
        redirect="/autores/"
    )
    
#endregion




#region Editor views
def editor_listado(request):
    form, datasource = SearchForm(request.GET), []
    # filter
    if form.is_valid():
        cd = form.cleaned_data
        if not cd['q']:
            datasource = Editor.objects.all().values()
        else:
            datasource = Editor.objects.filter(
                Q(nombre__icontains=cd['q']) |
                Q(ciudad__icontains=cd['q']) |
                Q(estado__icontains=cd['q']) |
                Q(pais__icontains=cd['q'])
            ).values()
    return render(request, "editor_listado.html", {
        "buscador": form,
        "object_list": datasource,
        "fields": [
            { "label": "Nombre",        "key": "nombre" },
            { "label": "Domicilio",     "key": "domicilio" },
            { "label": "Ciudad",        "key": "ciudad" },
            { "label": "Estado",        "key": "estado" },
            { "label": "Pais",          "key": "pais" },
            { "label": "Sitio oficial", "key": "website", "is_link":True },
        ],
        "actions": {
            "create": { "label": "Crear Editor",     "redirect": "/crear/editor" },
            "update": { "label": "Modificar Editor", "redirect": "/modificar/editor" },
            "delete": { "label": "Eliminar Editor",  "redirect": "/eliminar/editor" },
        }
    })



def editor_form(request, editor_id=None):
    # Se verifica la existencia
    editor_instance = get_object_or_404(Editor, id=editor_id) if editor_id else None
    # Update/create
    if request.method == "POST":
        form = EditorForm(request.POST, instance=editor_instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/editores")
    else:
        form = EditorForm(instance=editor_instance) if editor_instance else EditorForm()
    return render(request, "editor_form.html", {
        "form":   form,
        "action": "Modificar" if editor_instance else "Crear",
    })



def editor_delete(request, editor_id):
    editor = get_object_or_404(Editor, id=editor_id)
    return generic_delete(
        request=request,
        instance=editor,
        tpl_name="editor_delete.html",
        redirect="/editores/"
    )
#endregion




#region Libro views
def libro_listado(request):
    # Template context
    form, datasource = SearchForm(request.GET), []
    
    # filter
    if form.is_valid():
        cd = form.cleaned_data
        if not cd['q']:
            datasource = (Libro.objects
                .select_related("editor")
                .all()
            )
        else:
            datasource = (Libro.objects
                .select_related("editor")
                .filter(titulo__icontains=cd['q'])
            )
    return render(request, "libro_listado.html", {
        "buscador": form,
        "object_list": datasource,
    })



def libro_form(request, libro_id=None):
    # Se verifica la existencia del libro
    libro_instance = get_object_or_404(Libro, id=libro_id) if libro_id else None

    # Update/create
    if request.method == "POST":
        form = LibroForm(request.POST, request.FILES, instance=libro_instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/libros")
    else:
        form = LibroForm(instance=libro_instance) if libro_instance else LibroForm()

    return render(request, "libro_form.html", {
        "form":   form,
        "action": "Modificar" if libro_instance else "Crear",
    })



def libro_delete(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    return generic_delete(
        request=request,
        instance=libro,
        tpl_name="libro_delete.html",
        redirect="/libros/"
    )
#endregion


"""
---------------------------------------------------------------
Class based views
---------------------------------------------------------------
"""

#region autor clase-based views
class AutorListView(ListView):
    model = Autor
    template_name = "autor_listado__cbv.html"


class AutorCreateView(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = "autor_form__cbv.html"
    success_url = reverse_lazy("autores_cbv")


class AutorUpdateView(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = "autor_form__cbv.html"
    success_url = reverse_lazy("autores_cbv")


class AutorDeleteView(DeleteView):
    model = Autor
    form_class = AutorForm
    template_name = "autor_delete__cbv.html"
    success_url = reverse_lazy("autores_cbv")
#endregion




#region editor clase-based views
class EditorListView(ListView):
    model = Editor
    template_name = "editor_listado__cbv.html"


class EditorCreateView(CreateView):
    model = Editor
    form_class = EditorForm
    template_name = "editor_form__cbv.html"
    success_url = reverse_lazy("editores_cbv")


class EditorUpdateView(UpdateView):
    model = Editor
    form_class = EditorForm
    template_name = "editor_form__cbv.html"
    success_url = reverse_lazy("editores_cbv")


class EditorDeleteView(DeleteView):
    model = Editor
    form_class = EditorForm
    template_name = "editor_delete__cbv.html"
    success_url = reverse_lazy("editores_cbv")
#endregion




#region libro clase-based views
class LibroListView(ListView):
    model = Libro
    template_name = "libro_listado__cbv.html"
  

class LibroCreateView(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = "libro_form__cbv.html"
    success_url = reverse_lazy("libros_cbv")


class LibroUpdateView(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = "libro_form__cbv.html"
    success_url = reverse_lazy("libros_cbv")


class LibroDeleteView(DeleteView):
    model = Libro
    form_class = LibroForm
    template_name = "libro_delete__cbv.html"
    success_url = reverse_lazy("libros_cbv")
#endregion