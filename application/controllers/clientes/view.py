import web
import config as config


class View:
    def __init__(self):
        pass

    def GET(self, id_cliente):  
        clientes = config.model_clientes.select_cliente(id_cliente) # Selecciona el registro que coincida con id
        return config.render.view(clientes) # Envia el registro y renderiza view.html
