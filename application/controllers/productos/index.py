import web
import config as config


class Index:
    def __init__(self):
        pass

    def GET(self):  
        productos = config.model_productos.select_productos().list() # Selecciona todos los registros de productos
        return config.render.index(productos) # Envia todos los registros y renderiza index.html
