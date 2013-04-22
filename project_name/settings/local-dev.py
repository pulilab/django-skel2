import base

DEBUG = True
TEMPLATE_DEBUG = True
POST_MORTEM = True
FILER_DEBUG = True
FILER_ENABLE_LOGGING = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

SSL_ENABLED = False

INSTALLED_APPS = base.INSTALLED_APPS + (
    "django_pdb",
    "debug_toolbar",
    "django_nose",
)

MIDDLEWARE_CLASSES = base.MIDDLEWARE_CLASSES + (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django_pdb.middleware.PdbMiddleware',
)

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)
DEBUG_TOOLBAR_CONFIG = {"INTERCEPT_REDIRECTS": False}
INTERNAL_IPS = ('127.0.0.1',)

# run local smtp server with: python -m smtpd -n -c DebuggingServer localhost:1025
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
