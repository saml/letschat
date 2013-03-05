
EMAIL='you@your-company.com'
PASSWORD='yourpassword'
NICK='your-nickname'
ROOM='your-room@conference.your-company.com'

LOG_TRAFFIC = True

try:
    from settings_local import *
except ImportError:
    pass

