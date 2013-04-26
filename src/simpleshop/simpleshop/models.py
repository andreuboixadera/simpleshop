# -*- coding: utf-8 -*-

from pyramid.security import (
    Allow,
    Everyone,
    )

	

class RootFactory(object):
    __acl__ = [ (Allow, Everyone, 'view'),
		(Allow, 'group:usuaris', 'registrats'),
                (Allow, 'group:admins', 'administratius') ]
    def __init__(self, request):
        pass

