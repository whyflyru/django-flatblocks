from django.conf import settings

AUTOCREATE_STATIC_BLOCKS = getattr(settings,
                                   'FLATBLOCKS_AUTOCREATE_STATIC_BLOCKS',
                                   False)

CANCEL_ADMIN_AUTO_REGISTRATION = getattr(settings, 'CANCEL_ADMIN_AUTO_REGISTRATION', False)
