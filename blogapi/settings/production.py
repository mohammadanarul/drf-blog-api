from .base import *
import django_heroku
import dj_database_url

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', cast=bool)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['https://learnwithanarul.herokuapp.com/','*']

# database management
DATABASES = {'default': dj_database_url.config()}

# Configure Django App for Heroku.
django_heroku.settings(locals())

# whitenoise collectstatic
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_USE_TLS = config('EMAIL_USE_TLS')
EMAIL_BACKEND = config('EMAIL_BACKEND')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')

# cloudinary config  for heroku
# cloudinary.config( 
#   cloud_name = 'mohammadanarul',
#   api_key = '867477367854119', 
#   api_secret = 'Q4Wx4-s3DS9Zxf57tHk3uDX3WfY'
# )