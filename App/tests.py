import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TrabajoTitulacion.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import unittest
from App.models import Roles


# Create your tests here.

# Prueba crear rol
#class Test_Rol_Create(unittest.TestCase):
#    def test_crearRol(self):
#        print()

class test_Rol(unittest.TestCase):
    def test_create(self):
        res = Roles.objects.create(nombre="admin")
        #Roles.objects.create(nombre="profesor")
        #Roles.objects.create(nombre="estudiante")
        self.assertTrue(res.ok)


if __name__ == '__main__':
	unittest.main()