import json
from pathlib import Path
import environ

# 📁 Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# 🌱 Initialize environment
env = environ.Env()

# ✅ Load .env for local development (DEBUG=True)
# It will NOT be used when deployed with Azure App Settings (DEBUG=False)
try:
    DEBUG = env.bool("DJANGO_DEBUG", default=True)

    if DEBUG:
        env.read_env(BASE_DIR / ".env")
except Exception as e:
    print(f"[⚠️] Could not load .env file: {e}")
    DEBUG = True  # Fallback for dev safety

# 🔐 Core security settings
SECRET_KEY = env("DJANGO_SECRET_KEY", default="unsafe-default-key")
DEBUG = env.bool("DJANGO_DEBUG", default=True)

# 🌍 Host configuration
try:
    ALLOWED_HOSTS = json.loads(env("DJANGO_ALLOWED_HOSTS", default='["localhost", "127.0.0.1"]'))
except json.JSONDecodeError:
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

try:
    CSRF_TRUSTED_ORIGINS = json.loads(env("CSRF_TRUSTED_ORIGINS", default="[]"))
except json.JSONDecodeError:
    CSRF_TRUSTED_ORIGINS = []

# 🗄️ Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require',
        },
    }
}

LOGIN_URL = '/auth/login/'

# 📦 Installed apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # 🧩 Project apps
    "home",
    "construction_department",
    "sales_department",
    "project",
    "customer",
'azure_auth',
'django.contrib.sites',  # Required by django-azure-auth
]

AUTHENTICATION_BACKENDS = [
    'azure_auth.backends.AzureActiveDirectoryBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# Load environment-specific Azure AD credentials
AZURE_APP_CONTEXT = os.getenv("AZURE_APP_CONTEXT", "construction")  # Fallback to construction

if AZURE_APP_CONTEXT == "construction":
    AZURE_AUTH = {
        "CLIENT_ID": os.getenv("AZURE_CONSTRUCTION_CLIENT_ID"),
        "CLIENT_SECRET": os.getenv("AZURE_CONSTRUCTION_CLIENT_SECRET"),
        "TENANT_ID": os.getenv("AZURE_TENANT_ID"),
        "AZURE_REDIRECT_URI": "https://ds-erp-app.azurewebsites.net/auth/construction_redirect",
        "ROLES": {
            "aad-group-id-of-ConstructionDept": "ConstructionGroup"
        },
        "GROUPS_REQUIRED": True,
        "LOGIN_REDIRECT_URL": "/construction/dashboard/",
    }

elif AZURE_APP_CONTEXT == "sales":
    AZURE_AUTH = {
        "CLIENT_ID": os.getenv("AZURE_SALES_CLIENT_ID"),
        "CLIENT_SECRET": os.getenv("AZURE_SALES_CLIENT_SECRET"),
        "TENANT_ID": os.getenv("AZURE_TENANT_ID"),
        "AZURE_REDIRECT_URI": "https://ds-erp-app.azurewebsites.net/auth/sales_redirect",
        "ROLES": {
            "aad-group-id-of-SalesDept": "SalesGroup"
        },
        "GROUPS_REQUIRED": True,
        "LOGIN_REDIRECT_URL": "/sales/dashboard/",
    }

# ⚙️ Middleware stack
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    *(["whitenoise.middleware.WhiteNoiseMiddleware"] if not DEBUG else []),
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# 🔗 URLs and WSGI
ROOT_URLCONF = "ds_garden.urls"
WSGI_APPLICATION = "ds_garden.wsgi.application"

# 🎨 Templates
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

# 🔒 Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", "OPTIONS": {"min_length": 12}},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# 🌍 Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Dhaka"
USE_I18N = True
USE_TZ = True

# 📁 Static files
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

if not DEBUG:
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# 🆔 Default primary key field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"










