import os
from collections import OrderedDict
from datetime import timedelta
from pathlib import Path

from celery.schedules import crontab
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY", "")

DEBUG = bool(int(os.environ.get("DEBUG", "0")))

ALLOWED_HOSTS = ["*"]
CORS_ORIGIN_ALLOW_ALL = True
CSRF_TRUSTED_ORIGINS = [
    "https://develop.athayoga.su",
    "https://stage.athayoga.su",
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8080",
]

READING_SPEED = 180  # words per min.
MAX_ONLINE_PARTICIPANTS = 100
CONFIRMATION_TOKEN_LENGTH = 6

# Application definition

INSTALLED_APPS = [
    "base",
    "captcha",
    "django.contrib.admin",
    "django.contrib.auth",
    "polymorphic",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "core",
    "courses",
    "articles",
    "rest_framework",
    "drf_spectacular",
    "corsheaders",
    "django_extensions",
    "django_elasticsearch_dsl",
    "django_json_widget",
    "djangocms_admin_style",
    "django.contrib.sites",
    "cms",
    "menus",
    "treebeard",
    "sekizai",
    "easy_thumbnails",
    "djangocms_text_ckeditor",
    "ckeditor",
    "mptt",
    "django_mptt_admin",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "cms.middleware.user.CurrentUserMiddleware",
    "cms.middleware.page.CurrentPageMiddleware",
    "cms.middleware.toolbar.ToolbarMiddleware",
    "cms.middleware.language.LanguageCookieMiddleware",
    "cms.middleware.utils.ApphookReloadMiddleware",
    "django.middleware.locale.LocaleMiddleware",
]

ROOT_URLCONF = "server.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["journal/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "sekizai.context_processors.sekizai",
                "cms.context_processors.cms_settings",
                "django.template.context_processors.i18n",
            ],
        },
    },
]

WSGI_APPLICATION = "server.wsgi.application"

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_THROTTLE_CLASSES": [
        "core.custom_middleware.CustomAnonRateThrottle",
        "core.custom_middleware.CustomUserRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {"anon": "100/min", "user": "100/min"},
    "DEFAULT_THROTTLE_DENIED_DURATION": "600",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "EXCEPTION_HANDLER": "core.app.utils.exceptions.custom_exception_handler",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "ATHA Yoga API",
    "DESCRIPTION": "Atha yoga",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "COMPONENT_SPLIT_REQUEST": True,
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=7),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=8),
}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", ""),
        "USER": os.environ.get("POSTGRES_USER", ""),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", ""),
        "HOST": os.environ.get("POSTGRES_HOST", ""),
        "PORT": os.environ.get("POSTGRES_PORT", ""),
    }
}
AUTH_USER_MODEL = "core.User"

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

LANGUAGE_CODE = "ru-ru"
TIME_ZONE = "UTC"
USE_I18N = True
USE_T10N = True
USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

DEFAULT_PER_PAGE = 15

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_SSL = True

ELASTICSEARCH_DSL = {
    "default": {
        "hosts": f"{os.environ.get('ELASTIC_LOGIN')}:{os.environ.get('ELASTIC_PASSWORD')}@"
        f"{os.environ.get('ELASTIC_HOST')}:{os.environ.get('ELASTIC_PORT')}"
    },
}

TERMINAL_KEY = os.getenv("TERMINAL_KEY")
TERMINAL_PASSWORD = os.getenv("TERMINAL_PASSWORD")

SITE_URL = os.environ.get("SITE_URL")
BACKEND_URL = os.environ.get("BACKEND_URL")

RECAPTCHA_PUBLIC_KEY = os.getenv("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = os.getenv("RECAPTCHA_PRIVATE_KEY")
RECAPTCHA_DEFAULT_ACTION = "generic"
RECAPTCHA_SCORE_THRESHOLD = 0.8

LOGGING = {
    "version": 1,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "Time: {asctime} \n Module: {module} \n Line: {lineno} \n Message: {message} \n",
            "style": "{",
        },
    },
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "handlers": {
        "console": {
            "formatter": "verbose",
            "class": "logging.StreamHandler",
        },
        "app_log": {
            "class": "logging.FileHandler",
            "filename": os.path.join(BASE_DIR, "core/logs/app_log.log"),
            "formatter": "simple",
            "level": "DEBUG",
        },
        "daily_file": {
            "level": "ERROR",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "core/logs/daily_log.log"),
            "when": "D",
            "interval": 1,
            "backupCount": 10,
            "formatter": "simple",
        },
    },
    "loggers": {
        "app_log": {"handlers": ["app_log"], "propagate": False, "level": "DEBUG"},
        "daily_log": {"handlers": ["daily_file"], "propagate": False, "level": "ERROR"},
        "default_log": {"handlers": ["console"], "propagate": False, "level": "INFO"},
        "django": {
            "handlers": ["console"],
            "propagate": True,
            "level": "INFO",
        },
    },
}

DEFAULT_SUPERUSER_PASSWORD = os.environ.get("POSTGRES_PASSWORD")

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": os.path.join(BASE_DIR, "cache"),
        "TIMEOUT": 86400,
    }
}


COURSE_LESSONS_CYCLE = timedelta(days=60)

RESCHEDULE_CANCEL_COUNT_PERCENT = 0.25

MAX_FINE = 0.25
RATE_FINES_MAPPING = OrderedDict(
    {
        0.025: timedelta(hours=24),
        0.05: timedelta(hours=12),
        0.1: timedelta(hours=6),
        0.15: timedelta(hours=1),
    }
)

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", "")
CELERY_BROKER_TRANSPORT = os.environ.get("CELERY_BROKER_TRANSPORT", "amqp")
CELERY_BROKER_TRANSPORT_OPTIONS = {
    "visibility_timeout": 3600,
    "polling_interval": 60,
    "region": os.environ.get("CELERY_BROKER_TRANSPORT_REGION", "ru-central1"),
    "queue_name_prefix": "atha-",
}
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND")
CELERY_BEAT_SCHEDULE = {
    "end-courses-task": {
        "task": "courses.tasks.end_courses_task",
        "schedule": crontab(
            hour="*/6",
            minute=0,
        ),
    },
}
CELERY_TASK_DEFAULT_QUEUE = "default"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_SERIALIZER = "json"

SITE_ID = 1
LANGUAGES = [
    ("ru-ru", "Russian"),
]
X_FRAME_OPTIONS = "SAMEORIGIN"

CMS_TEMPLATES = [
    ("fullwidth.html", "Fullwidth"),
    ("sidebar_left.html", "Sidebar Left"),
    ("sidebar_right.html", "Sidebar Right"),
]

THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    "easy_thumbnails.processors.colorspace",
    "easy_thumbnails.processors.autocrop",
    "filer.thumbnail_processors.scale_and_crop_with_subject_location",
    "easy_thumbnails.processors.filters",
)
