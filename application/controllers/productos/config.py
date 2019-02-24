import web # importa la libreria web.py
import application.models.model_productos as model_productos # importa el modelo_productos


render = web.template.render('application/views/productos/', base='master') # configura la ubicacion de las vistas