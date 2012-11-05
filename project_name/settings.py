from settings_common import *

INSTALLED_APPS = INSTALLED_APPS + (
    'raven.contrib.django',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'handlers': {
        'mail_admins': {
            'level': 'WARNING',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'sentry': {
            'level': 'WARNING',
            'class': 'raven.contrib.django.handlers.SentryHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'WARNING',
            'propagate': True,
        },
    }
}

SENTRY_DSN = 'http://user:password@ip.address:port'