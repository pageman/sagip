"""
Django settings for sagip project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't#i^(67xf^1mru#&q^g-x2%2=!zst!=q2*89@u+3in^ta%g#6h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sagip_main',
##    'sagip_auth',
#    'app',
    'social.apps.django_app.default',
    
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sagip.urls'

WSGI_APPLICATION = 'sagip.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

AUTHENTICATION_BACKENDS = (
   'social.backends.facebook.FacebookOAuth2',
   'social.backends.google.GoogleOAuth2',
   'social.backends.twitter.TwitterOAuth',
   'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

TEMPLATE_CONTEXT_PROCESSORS = (
   'django.contrib.auth.context_processors.auth',
   'django.core.context_processors.debug',
   'django.core.context_processors.i18n',
   'django.core.context_processors.media',
   'django.core.context_processors.static',
   'django.core.context_processors.tz',
   'django.contrib.messages.context_processors.messages',
   'social.apps.django_app.context_processors.backends',
   'social.apps.django_app.context_processors.login_redirect',
)

LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_TWITTER_KEY = 'dERngpxJdPsRm9X6jb3o59CjQ'
SOCIAL_AUTH_TWITTER_SECRET = 'XsmDsEBIMThbuBSB17Id9gSWvWXb8SKYWuSS0jdpWzSZQEs09R'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '526323029748-p3amf2punr4r655a5o9ccudentv8aoad.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'lCExTcXZrmnLTZ1BURMiJwk9' 

#SOCIAL_AUTH_PIPELINE = (
#    'social.pipeline.social_auth.social_details',
#    'social.pipeline.social_auth.social_uid',
#    'social.pipeline.social_auth.auth_allowed',
#    'social_auth.backends.pipeline.social.social_auth_user',
#    'social_auth.backends.pipeline.associate.associate_by_email',
#    'social_auth.backends.pipeline.misc.save_status_to_session',
#    'sagip_auth.pipeline.redirect_to_form',
#    'sagip_auth.pipeline.username',
#    'social_auth.backends.pipeline.user.create_user',
#    'social_auth.backends.pipeline.social.associate_user',
#    'social_auth.backends.pipeline.social.load_extra_data',
#    'social_auth.backends.pipeline.user.update_user_details',
#    'sagip_auth.pipeline.redirect_to_form2',
#    'sagip_auth.pipeline.first_name',
#)
#SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'

#try:
##    from sagip_auth.local_settings import *
#    from app.local_settings import * 
#except Exception as e:
#    pass
