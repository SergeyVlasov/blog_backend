from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "dev-secret-key"
DEBUG = True

ALLOWED_HOSTS = ["*"]


# ─────────────────────────
# APPS
# ─────────────────────────
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # third party
    "ninja",
    "ninja_jwt",

    # local apps
    "apps.users",
    "apps.posts",
    "apps.comments",
    "apps.categories",
]


# ─────────────────────────
# AUTH
# ─────────────────────────
AUTH_USER_MODEL = "users.User"


# ─────────────────────────
# MIDDLEWARE
# ─────────────────────────
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]


ROOT_URLCONF = "config.urls"


# ─────────────────────────
# TEMPLATES (admin needs it)
# ─────────────────────────
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# ─────────────────────────
# DATABASE (PostgreSQL via docker)
# ─────────────────────────
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "blog",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "127.0.0.1",
        "PORT": 5432,
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ─────────────────────────
# PASSWORDS
# ─────────────────────────
AUTH_PASSWORD_VALIDATORS = []


# ─────────────────────────
# INTERNATIONALIZATION
# ─────────────────────────
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# ─────────────────────────
# STATIC
# ─────────────────────────
STATIC_URL = "static/"


# ─────────────────────────
# LOGGING
# ─────────────────────────
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "app.log",
        },
    },
    "loggers": {
        "apps": {
            "handlers": ["console", "file"],
            "level": "INFO",
        },
        "django": {
            "handlers": ["console"],
            "level": "INFO",
        },
    },
}
