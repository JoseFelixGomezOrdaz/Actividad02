import web
import config as config


class Update:
    def __init__(self):
        pass

    def GET(self, id_cliente): 
        clientes = config.model_clientes.select_cliente(id_cliente) # Selecciona el registro que coincida con id
        return config.render.update(clientes) # Envia el registro y renderiza update.html
    
    def POST(self, id_cliente, nombre_cliente, apellido_paterno, apellido_materno, telefono):
        formulario= web.input() # almacena los datos del formulario
        id_cliente=formulario['id_cliente'] # almacena el nombre escrito en el input
        nombre_cliente= formulario['nombre_cliente'] # almacena el nombre escrito en el input
        apellido_paterno= formulario['apellido_paterno'] # almacena el apellido en el imput
        apellido_materno= formulario['apellido_materno'] # almacena el apellido en el input
        telefono= formulario['telefono'] # almacena el telefono en el input
        config.model_clientes.update_cliente(id_cliente, nombre_cliente, apellido_paterno, apellido_materno, telefono) # llama al metodo insert_datos y le paso los datos guardados
        raise web.seeother('/clientes') # redirecciona al index
