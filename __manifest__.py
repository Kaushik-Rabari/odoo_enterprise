{
    'name': 'Session Logout on Browser Close',
    'version': '17.0.1.0.0',
    'category': 'Tools',
    'summary': 'Logs out the user when the browser is closed',
    'depends': ['base','web'],
    'data': [],
    'assets': {
        'web.assets_backend': [
            'session_logouter/static/src/js/custom_logout.js',
        ],
    },
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
}