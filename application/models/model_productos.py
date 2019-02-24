import config as config # importa el archivo config

db = config.db # crea un objeto db del objeto db creado en config

'''
Metodo para seleccionar todos los registros de la tabla productos
'''
def select_productos():
    try:
        return db.select('productos') # Selecciona todos los registros de la tabla productos
    except Exception as e:
        print "Model select_productos Error {}".format(e.args)
        print "Model select_productos Message {}".format(e.message)
        return None

'''
Metodo para seleccionar un registro que coincida con el id
'''
def select_producto(id_producto):
    try:
        return db.select('productos',where='id_producto=$id_producto', vars=locals())[0] # selecciona el primer registro que coincida con el id
    except Exception as e:
        print "Model select_productos Error {}".format(e.args)
        print "Model select_productos Message {}".format(e.message)
        return None

'''
Metodo para insertar un nuevo registro usando nombre, marca, modelo, cantidad
'''
def insert_producto(nombre, marca, modelo, cantidad):
    try:
        return db.insert('productos', nombre=nombre, marca=marca, modelo=modelo, cantidad=cantidad) # inserta un registro en productos
    except Exception as e:
        print "Model insert_productos Error {}".format(e.args)
        print "Model insert_productos Message {}".format(e.message)
        return None

'''
Metodo para eliminar un registro que coincida con el id
'''
def delete_producto(id_producto):
    try:
        return db.delete('productos', where='id_producto=$id_producto',vars=locals()) # borra un registro de productos
    except Exception as e:
        print "Model delete_productos Error {}".format(e.args)
        print "Model delete_productos Message {}".format(e.message)
        return None

'''
Metodo para actualizar el nombre, marca, modelo, cantidad
'''
def update_producto(id_producto, nombre, marca, modelo, cantidad): # actualiza datos que coincidan con el id
    try:
        return db.update('productos', nombre=nombre, marca=marca, modelo=modelo, cantidad=cantidad,  
            where='id_producto=$id_producto',
            vars=locals())
    except Exception as e:
        print "Model update_productos Error {}".format(e.args)
        print "Model update_productos Message {}".format(e.message)
        return None