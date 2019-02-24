import web
import config as config


class Delete:
    def __init__(self):
        pass

    def GET(self, id_producto): 
        productos = config.model_productos.select_producto(id_producto) # Selecciona el registro que coincida con id_producto
        return config.render.delete(productos) # Envia el registro y renderiza delete.html
    
    def POST(self, id_producto):
        formulario = web.input() # Crea un objeto formuario con los datos enviados con el formulario
        id_producto = formulario['id_producto'] # Obtine el id_producto almacenado en el formulario
        config.model_productos.delete_producto(id_producto) # Borra el registro del id_producto seleccionado
        raise web.seeother('/productos') # Redirecciona a raiz
