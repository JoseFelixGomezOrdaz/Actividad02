import web
import config as config


class Delete:
    def __init__(self):
        pass

    def GET(self, id_cliente): 
        clientes = config.model_clientes.select_cliente(id_cliente) # Selecciona el registro que coincida con id_cliente
        return config.render.delete(clientes) # Envia el registro y renderiza delete.html
    
    def POST(self, id_cliente):
        formulario = web.input() # Crea un objeto formuario con los datos enviados con el formulario
        id_cliente = formulario['id_cliente'] # Obtine el id_cliente almacenado en el formulario
        config.model_clientes.delete_cliente(id_cliente) # Borra el registro del id_cliente seleccionado
        raise web.seeother('/clientes') # Redirecciona a raiz
