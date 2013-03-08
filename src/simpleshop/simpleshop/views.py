from pyramid.view import view_config
from DadesProductes import Productes
from pyramid.httpexceptions import HTTPFound


@view_config(route_name='list', renderer='list.mako')			# Generar llista de productes
def list_view(request):	
							
        productes = Productes()
        claus = productes.getProducteKeys()
 
	tasks = {}


    	tasks = [dict(id=row, nom=productes.getProducteNOM(str(row)), stock=productes.getProducteSTOCK(str(row)), preu=productes.getProductePREU(str(row)))  for row in claus]


        return {'tasks': tasks}





@view_config(route_name='new', renderer='new.mako')			# Affegir productes (mitjancant objecte Producte)
def new_view(request):
	if request.method == 'POST':

		productes = Productes()

                productes.guardarproducte(request.POST['id'],request.POST['nom'],request.POST['quantitat'],request.POST['preu'])



		request.session.flash('Producte affegit correctament!')
		return HTTPFound(location=request.route_url('list'))
        else:
		request.session.flash('Entra les dades del producte')

	return {}





@view_config(route_name='close')					# Eliminar producte fitxer per ID
def close_view(request):
	
	task_id = int(request.matchdict['id'])

	productes = Productes()
        productes.eliminarproducte(task_id)

	request.session.flash('Producte eliminat!')
	return HTTPFound(location=request.route_url('list'))



@view_config(context='pyramid.exceptions.NotFound', renderer='notfound.mako')	# Redireccio pagina no trobada
def notfound_view(self):
    return {}




@view_config(route_name='modify', renderer='modify.mako')		# Modificar producte per ID
def modify_view(request):
	
	task_id = str(request.matchdict['id'])
	
	if request.method == 'POST':
		productes = Productes()
       		productes.modificaproducte(task_id, request.POST['nom'], request.POST['quantitat'], request.POST['preu'])

		request.session.flash('Producte modificat!')
		return HTTPFound(location=request.route_url('list'))

        else:
		request.session.flash('Entra les dades del producte')

	return {}



@view_config(route_name='buy', renderer='comanda.mako')		# Realitzar comanda
def buy_view(request):
	
	productes = Productes()
        claus = productes.getProducteKeys()

	idcomanda = productes.carregaCommanda()
 

	if request.method == 'POST':

		for clau in claus:

			nom=productes.getProducteNOM(str(clau)) 
			preu=productes.getProductePREU(str(clau))
			productes.guardarcomanda(idcomanda, clau, nom, request.POST[clau], preu)


		productes.seguentcomanda(idcomanda)

		request.session.flash('Comanda desada!')
		return HTTPFound(location=request.route_url('buy'))



	tasks = {}

    	tasks = [dict(id=row, nom=productes.getProducteNOM(str(row)), stock=productes.getProducteSTOCK(str(row)), preu=productes.getProductePREU(str(row)))  for row in claus]

        return {'tasks': tasks, 'idcomanda':idcomanda}
