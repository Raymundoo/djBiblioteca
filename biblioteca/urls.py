"""djbiblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
# Local imports
from biblioteca import views

urlpatterns = [
    url(r'^$', views.autor_listado),
    
    url(r'^autores$', views.autor_listado),
    url(r'^crear/autor$', views.autor_cu),
    url(r'^modificar/autor/(\d+)$', views.autor_cu),
    url(r'^eliminar/autor$', views.autor_delete),
    
    url(r'^editores$', views.editor_listado),
    url(r'^crear/editor$', views.editor_cu),
    url(r'^modificar/editor/(\d+)$', views.editor_cu),
    url(r'^eliminar/editor$', views.editor_delete),
    
    url(r'^libros$', views.libro_listado),
    url(r'^crear/libro$', views.autor_cu),
    url(r'^modificar/libro/(\d+)$', views.autor_cu),
    url(r'^eliminar/libro$', views.libro_delete),
]
