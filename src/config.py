import os, logging

DEBUG = True
HOST = os.getenv('HOST', '0.0.0.0')
PORT = int(os.getenv('PORT', '5000'))

POSTGRES = {
    'user': os.getenv('POSTGRES_USER', 'api'),
    'pw': os.getenv('POSTGRES_PW', ''),
    'host': os.getenv('POSTGRES_HOST', 'localhost'),
    'port': os.getenv('POSTGRES_PORT', '5432'),
    'db': os.getenv('POSTGRES_DB', 'velib_statistics'),
}
DB_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

logging.basicConfig(
    filename=os.getenv('SERVICE_LOG', 'server.log'),
    level=logging.DEBUG,
    format='%(levelname)s: %(asctime)s pid:%(process)s module:%(module)s %(message)s',
    datefmt='%d/%m/%y %H:%M:%S',
)

APPLICATION_ROOT = os.getenv('APPLICATION_ROOT', '/velib-statistics')

VELIB_API_URL = os.getenv('VELIB_API_URL', 'https://api.jcdecaux.com/vls/v1')
VELIB_API_KEY = os.getenv('VELIB_API_KEY', '')
