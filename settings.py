from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [

    {
        'name': 'ug_gui',
        'display_name': "Ultimatum GUI",
        'num_demo_participants': 2,
        'app_sequence': ['ug_gui'],
        'use_strategy_method': False,
    },
{
        'name': 'ug_text',
        'display_name': "Ultimatum Text",
        'num_demo_participants': 2,
        'app_sequence': ['ug_text'],
        'use_strategy_method': False,
    },
{
        'name': 'ug_gui_no_wait',
        'display_name': "Ultimatum GUI no wait",
        'num_demo_participants': 2,
        'app_sequence': ['ug_gui_no_wait'],
        'use_strategy_method': False,
    },
{
        'name': 'ug_gui_nyuad',
        'display_name': "Ultimatum GUI NYUAD",
        'num_demo_participants': 2,
        'app_sequence': ['ug_gui_nyuad'],
        'use_strategy_method': False,
    },

]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'INR'
USE_POINTS = True

ROOMS = []


# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

SENTRY_DSN = environ.get('SENTRY_DSN')

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


# Consider '', None, and '0' to be empty/false
DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})

DEMO_PAGE_INTRO_HTML = """ """

# don't share this with anybody.
SECRET_KEY = 'kht^8^b77s#sd(1)y69u$s*pqcb@@%b=+7&i17b-+_@5vm^_z_'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
