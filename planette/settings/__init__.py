from .base import *

env = os.environ.get('PFI_ENV', '')

if env == 'TESTING':
    print('Using TESTING environment settings')
    try:
        from .testing import *
    except:
        pass

elif env == 'PRODUCTION':
    print('Using PRODUCTION environment settings')
    try:
        from .production import *
    except:
        pass
