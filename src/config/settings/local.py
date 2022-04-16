from distutils.util import strtobool
from ..utils import get_secret
from .base import *


DEBUG = True

THIRD_PARTY_LOCAL_APPS = [
    'debug_toolbar'
]
ENABLED_SWAGGER_DOC = True

INSTALLED_APPS += THIRD_PARTY_LOCAL_APPS

# DEBUG TOOLBAR CONFIG
MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

# DEBUG TOOLBAR HACK FOR DOCKER
if DEBUG:
    import os  # only if you haven't already imported this
    import socket  # only if you haven't already imported this
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]
