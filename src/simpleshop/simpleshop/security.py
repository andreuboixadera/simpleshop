USERS = {'usuari':'usuari',
	'admin':'admin',}
GROUPS = {'admin':['group:admins','group:usuaris'],
	'usuari':['group:usuaris'],}

def groupfinder(userid, request):
    if userid in USERS:
        return GROUPS.get(userid, [])


def comprova_usuari(userid, passw):

    if USERS.get(userid)==passw:
        return True
    return False
