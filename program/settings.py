from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

SESSION_CONFIGS = [
     dict(
        name='CRT',
        display_name="Cognitive Reflection Test",
        num_demo_participants=1,
        app_sequence=['CRT']
     ),
     dict(
        name='BIG5',
        display_name="BIG5",
        num_demo_participants=1,
        app_sequence=['BIG5']
     ),
     dict(
        name='REI',
        display_name="情報処理スタイル尺度（短縮版）",
        num_demo_participants=1,
        app_sequence=['REI']
     ),
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'JPY'
USE_POINTS = True

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'qha1oxs0rb%pf%267m$c8pp7x6xtv8raq#%_p_f2mzp808x@7*'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
