import web
import config as config


class Insert:
    def __init__(self):
        pass

    def GET(self):  
        return config.render.insert() # renderiza la pagina insert.html
    
    def POST(self):
        formulario= web.input() # almacena los datos del formulario
        nombre_cliente= formulario['nombre_cliente'] # almacena el nombre escrito en el input
        apellido_paterno= formulario['apellido_paterno'] # almacena el apellido en el imput
        apellido_materno= formulario['apellido_materno'] # almacena el apellido en el input
        telefono= formulario['telefono'] # almacena el telefono en el input
        config.model_clientes.insert_cliente(nombre_cliente, apellido_paterno, apellido_materno, telefono) # llama al metodo insert_datos y le paso los datos guardados
        raise web.seeother('/clientes') # redirecciona al index.html
