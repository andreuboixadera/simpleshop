from pyramid.httpexceptions import HTTPFound

from pyramid.view import (
    view_config,
    forbidden_view_config,
)
from pyramid.security import (
    remember,
    forget,
    authenticated_userid,
)
from .security import comprova_usuari

from DadesProductes import Productes


#INICI
@view_config(route_name='benvingut', renderer='benvingut.mako', permission='view')
def benvingut_view(request):
    return { 'logged_in':authenticated_userid(request) }



@view_config(route_name='list', renderer='list.mako', permission='administratius')		# Generar llista de productes admin
def list_view(request):	
							
        productes = Productes()
        claus = productes.getProducteKeys()
 
	tasks = {}


    	tasks = [dict(id=row, nom=productes.getProducteNOM(str(row)), stock=productes.getProducteSTOCK(str(row)), preu=productes.getProductePREU(str(row)))  for row in claus]


        return {'tasks': tasks, 'page':"Llistat Administracio", 'logged_in':authenticated_userid(request)}




@view_config(route_name='comandas', renderer='comandas.mako', permission='registrats')		
def comandas_view(request):	
							
        productes = Productes()

	registre = productes.getLlistaComandes()




	dades = registre.split("\n")

	tasks =[dict(contingut=row) for row in dades]
		

	return {'tasks': tasks, 'page':"Llista Comandes", 'logged_in':authenticated_userid(request)}




@view_config(route_name='new', renderer='new.mako', permission='administratius')			# Affegir productes (mitjancant objecte Producte)
def new_view(request):
	if request.method == 'POST':

		productes = Productes()

                productes.guardarproducte(request.POST['id'],request.POST['nom'],request.POST['quantitat'],request.POST['preu'])



		
		return HTTPFound(location=request.route_url('list'))
        else:
		pass
		

	return {'logged_in':authenticated_userid(request)}





@view_config(route_name='close', permission='administratius')					# Eliminar producte fitxer per ID
def close_view(request):
	
	task_id = int(request.matchdict['id'])

	productes = Productes()
        productes.eliminarproducte(task_id)

	return HTTPFound(location=request.route_url('list'))



@view_config(context='pyramid.exceptions.NotFound', renderer='notfound.mako')		# Redireccio pagina no trobada
def notfound_view(self):
	return {}



@view_config(route_name='modify', renderer='modify.mako', permission='administratius')		# Modificar producte per ID
def modify_view(request):
	
	task_id = str(request.matchdict['id'])
	
	if request.method == 'POST':
		productes = Productes()
       		productes.modificaproducte(task_id, request.POST['nom'], request.POST['quantitat'], request.POST['preu'])

		return HTTPFound(location=request.route_url('list'))

        else:
		pass

	return {'page' : "Modificar Producte", 'logged_in' : authenticated_userid(request)}



@view_config(route_name='buy', renderer='comanda.mako', permission='registrats' )				# Realitzar comanda
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

		return HTTPFound(location=request.route_url('buy'))



	tasks = {}

    	tasks = [dict(id=row, nom=productes.getProducteNOM(str(row)), stock=productes.getProducteSTOCK(str(row)), preu=productes.getProductePREU(str(row)))  for row in claus]

        return {'tasks': tasks, 'idcomanda':idcomanda, 'logged_in':authenticated_userid(request)}

@view_config(route_name='login', renderer='login.mako')

@forbidden_view_config(renderer='login.mako')
def login(request):
    login_url = request.route_url('login')
    # detectem des de quina URL ve el visitant
    referrer = request.url
    # retornem l'usuari a la home page si ha vingut directe al login
    if referrer == login_url:
        referrer = '/' # never use the login form itself as came_from
    came_from = request.params.get('came_from', referrer)
    user = authenticated_userid(request)
    if user:
        lloc = came_from.split("/")
        message = "Ets %s, i com a tal no pots entrar a %s" % (user,lloc[len(lloc)-1])
    else:
        message = "Identifica't per entrar al sagrat mon d'Egipte"
    login = ''
    password = ''
    if 'form.submitted' in request.params:
        login = request.params['login']
        password = request.params['password']
        if comprova_usuari(login,password):
            headers = remember(request, login)
            return HTTPFound(location = came_from,
                             headers = headers)
        message = 'Failed login'

    return dict(
        message = message,
        url = request.application_url + '/login',
        came_from = came_from,
        login = login,
        password = password,
        user = authenticated_userid(request), # afegim usuari autenticat si l'hi ha
        )
    

@view_config(route_name='logout')
def logout(request):
    headers = forget(request)
    return HTTPFound(location = request.route_url('benvingut'),
                     headers = headers)
