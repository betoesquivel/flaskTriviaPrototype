import os
from authomatic.providers import oauth2

FBAPPKEY = os.environ.get('FACEBOOK_APP_ID')
FBAPPSECRET = os.environ.get('FACEBOOK_SECRET')
CONFIG = {
    'fb': {

        'class_': oauth2.Facebook,
        'id':1,
        # Facebook is an AuthorizationProvider too.
        'consumer_key': FBAPPKEY,
        'consumer_secret': FBAPPSECRET,

        # But it is also an OAuth 2.0 provider and it needs scope.
        'scope': ['user_about_me', 'email', 'publish_stream'],
    }
}
