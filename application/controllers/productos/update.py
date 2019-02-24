import web
import config as config


class Update:
    def __init__(self):
        pass

    def GET(self, id_producto): 
        productos = config.model_productos.select_producto(id_producto) # Selecciona el registro que coincida con id
        return config.render.update(productos) # Envia el registro y renderiza update.html
    
    def POST(self, id_producto, nombre, marca, modelo, cantidad):
        formulario= web.input() # almacena los datos del formulario
        id_producto=formulario['id_producto'] # almacena el id escrito en el input
        nombre= formulario['nombre'] # almacena el nombre escrito en el input
        marca= formulario['marca'] # almacena la marca en el imput
        modelo= formulario['modelo'] # almacena el modelo en el input
        cantidad= formulario['cantidad'] # almacena el cantidad en el input
        config.model_productos.update_producto(id_producto, nombe, marca, modelo, cantidad) # llama al metodo insert_datos y le paso los datos guardados
        raise web.seeother('/productos') # redirecciona al index
