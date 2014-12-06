# installer for the vds-bootstrap extension

from setup import ExtensionInstaller

def loader():
    return MySkinInstaller()

class MySkinInstaller(ExtensionInstaller):
    def __init__(self):
        super(MySkinInstaller, self).__init__(
            version="0.1",
            name='vds-bootstrap',
            description='vds vds-bootstrap skin, not to be confused with the other one(s) out there.',
            author="Vince Skahan",
            author_email="vinceskahan@gmail.com",
            config={
                'StdReport': {
                    'vds-bootstrap': {
                        'skin': 'vds-bootstrap',
                        'HTML_ROOT': 'bootstrap',
                        }
                }
            },
            files=[
                 ('skins/vds-bootstrap',
                    ['skins/vds-bootstrap/skin.conf',
                     'skins/vds-bootstrap/favicon.ico',
                      'skins/vds-bootstrap/index.html.tmpl',
                      'skins/vds-bootstrap/bootstrap-about.html.tmpl',
                      'skins/vds-bootstrap/bootstrap-alltime.html.tmpl',
                      'skins/vds-bootstrap/bootstrap-week.html.tmpl',
                      'skins/vds-bootstrap/bootstrap-forecast.html.tmpl',
                      'skins/vds-bootstrap/bootstrap-year.html.tmpl',
                      'skins/vds-bootstrap/bootstrap-month.html.tmpl',
                      'skins/vds-bootstrap/respond.min.js',
                      'skins/vds-bootstrap/skin.conf',
                      'skins/vds-bootstrap/sticky-footer-navbar.css',
                      'skins/vds-bootstrap/bootstrap.css',
                      'skins/vds-bootstrap/html5shiv.js',
                    ]
                 )
           ]
         )

