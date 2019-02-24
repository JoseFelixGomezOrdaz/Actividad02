import web
import config as config


class Insert:
    def __init__(self):
        pass

    def GET(self):  
        return config.render.insert() # renderiza la pagina insert.html
    
    def POST(self):
        formulario= web.input() # almacena los datos del formulario
        nombre= formulario['nombre'] # almacena el nombre escrito en el input
        marca= formulario['marca'] # almacena el marca en el imput
        modelo= formulario['modelo'] # almacena el modelo en el input
        cantidad= formulario['cantidad'] # almacena el cantidad en el input
        config.model_productos.insert_producto(nombre, marca, modelo, cantidad) # llama al metodo insert_datos y le paso los datos guardados
        raise web.seeother('/productos') # redirecciona al index.html
