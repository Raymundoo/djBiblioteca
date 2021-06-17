from django.forms.models import model_to_dict

class TableConfig():
    """
    Configuracion de la tabla
    """
    # Campos a motrar
    fields = []
    # Datos
    datasource = []
    # form
    form = None

    create_action = None
    update_action = None
    delete_action = None

