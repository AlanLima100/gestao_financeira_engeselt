"""
WSGI config for Controle_de_gastos project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# from dj_static import Cling, MediaCling # CLING = aprensta os arquivos statics CSS, HTML, JS e image do proprio website, MediaCling = apresenta os uplooad

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Controle_de_gastos.settings')

application = get_wsgi_application()
