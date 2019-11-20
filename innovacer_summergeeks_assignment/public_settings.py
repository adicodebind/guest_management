
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'rjm466f)oa8v5gbb%yd6gu(sdt#p5rac3r(wz)!1+csk*mvxmn'


DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SENDGRID_SANDBOX_MODE_IN_DEBUG = False
SENDGRID_API_KEY = "fake.api.key"

EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
EMAIL_HOST = "smtp.sendgrid.net"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "fake_user"
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
PUBLIC_ID_LENGTH = 10