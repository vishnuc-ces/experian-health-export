import os

dir = os.path.abspath(os.path.dirname(__file__))

SSL_KEY_PATH = os.path.join(dir, 'certs/client-key.pem')

SSL_CERT_PATH = os.path.join(dir, 'certs/client-cert.pem')

HOST = '35.193.96.41'

USERNAME = 'vishnuc.cesit'

PASSWORD = 'welcome123'

DATABASENAME = 'emr-data-locker'

SQLALCHEMY_TRACK_MODIFICATIONS = False

