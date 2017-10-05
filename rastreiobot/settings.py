from decouple import config


PLATFORMS = {
    'telegram': {
        'ENGINE': 'bottery.platform.telegram',
        'OPTIONS': {
            'token': config('TOKEN'),
        }
    },
}
