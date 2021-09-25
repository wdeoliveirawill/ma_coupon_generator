import os
from pathlib import Path
from dj_database_url import parse as parse_db_url
from prettyconf import config

BASE_DIR = Path(__file__).absolute().parents[2]
PROJECT_DIR = Path(__file__).absolute().parents[2]

SECRET_KEY = config("SECRET_KEY", default="yyyyxxxxzzzz", cast=str)
DEBUG = config("DEBUG", default=False, cast=bool)
LOG_LEVEL = config("LOG_LEVEL", default="INFO")
LOGGERS = config("LOGGERS", default="", cast=config.list)
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="*", cast=config.list)


INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django_extensions",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_use_email_as_username.apps.DjangoUseEmailAsUsernameConfig",
    "custom_user.apps.CustomUserConfig",
    "coupons",
    # apps
    # "apps.pages",
    # extra packages
    # "ajaximage",
    # "cuser",
    # "django_summernote",
    # "rest_framework",
    # "drf_spectacular",
    # "colorfield",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "maria_alice_coupon_generator.urls"
AUTH_USER_MODEL = "custom_user.User"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "maria_alice_coupon_generator.wsgi.application"


# DATABASES = {
#     "default": {
#         "ENGINE": config("DATABASE_ENGINE"),
#         "NAME": config("DATABASE_NAME"),
#         "USER": config("DATABASE_USER"),
#         "PASSWORD": config("DATABASE_PASSWORD"),
#         "HOST": config("DATABASE_HOST"),
#         "PORT": config("DATABASE_PORT"),
#     }
# }
# DATABASES["default"]["CONN_MAX_AGE"] = config("CONN_MAX_AGE", cast=config.eval, default="None")
# DATABASES["default"]["TEST"] = {"NAME": config("TEST_DATABASE_NAME", default=None)}

DATABASES = {"default": config("DATABASE_URL", cast=parse_db_url)}
DATABASES["default"]["CONN_MAX_AGE"] = config(
    "CONN_MAX_AGE", cast=config.eval, default="None"
)  # always connected
DATABASES["default"]["TEST"] = {"NAME": config("TEST_DATABASE_NAME", default=None)}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static/")]
STATIC_URL = "/static/"
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

JAZZMIN_SETTINGS = {
    "site_title": "Maria Alice | Gerador de Cupons",
    "site_header": "Gerador de Cupons",
    "site_brand": "Maria Alice",
    # "site_logo": "../static/imgs/logo.png",
    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",
    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,
    # Welcome text on the login screen
    "welcome_sign": "Bem-vindo",
    # Copyright on the footer
    "copyright": "Maria Alice",
    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "custom_user.User",
    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,
    "show_sidebar": True,
    "navigation_expanded": True,
}
