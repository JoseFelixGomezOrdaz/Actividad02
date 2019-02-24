import web
        
urls = (
    '/','application.controllers.clientes.home.Home',
    '/clientes', 'application.controllers.clientes.index.Index',
    '/insert', 'application.controllers.clientes.insert.Insert',
    '/update/(.*)', 'application.controllers.clientes.update.Update',
    '/delete/(.*)', 'application.controllers.clientes.delete.Delete',
    '/view/(.*)', 'application.controllers.clientes.view.View',

	'/productos', 'application.controllers.productos.index.Index',
	'/insertprod', 'application.controllers.productos.insert.Insert',
	'/updateprod/(.*)', 'application.controllers.productos.update.Update',
	'/deleteprod/(.*)', 'application.controllers.productos.delete.Delete',
	'/viewprod/(.*)', 'application.controllers.productos.view.View',
)

if __name__ == "__main__":
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()
