import os
import logging

from pyramid.config import Configurator

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from .security import groupfinder
from .models import RootFactory

from pyramid.events import NewRequest
from pyramid.events import subscriber
from pyramid.events import ApplicationCreated
from pyramid.httpexceptions import HTTPFound
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from pyramid.view import view_config

from DadesProductes import Productes

from wsgiref.simple_server import make_server

import sqlite3

logging.basicConfig()
log = logging.getLogger(__file__)

here = os.path.dirname(os.path.abspath(__file__))

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    #settings = {}
    #settings['reload_all'] = True
    #settings['debug_all'] = True
    settings['mako.directories'] = os.path.join(here, 'templates')
    #settings['db'] = os.path.join(here, 'tasks.db')

# routes setup
    authn_policy = AuthTktAuthenticationPolicy('sosecret', callback=groupfinder, hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    config = Configurator(root_factory='.models.RootFactory', settings=settings)
    #config = Configurator(settings=settings)
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)

   

    config.add_static_view('static', os.path.join(here, 'static'))
    config.add_route('benvingut', '/')
    config.add_route('buy', '/buy')
    config.add_route('list', '/admin')
    config.add_route('new', '/admin/new')
    config.add_route('close', '/admin/close/{id}')
    config.add_route('modify', '/admin/modify/{id}')
    config.add_route('comandas', '/comandas')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')




    # static view setup
    #config.add_static_view('static', os.path.join(here, 'static'))
    # scan for @view_config and @subscriber decorators
    config.scan()
    return config.make_wsgi_app()


