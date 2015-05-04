from django.conf import settings

# django-fullcalendar static file location defaults to FullCalendar default 
# folder structure, expected to be under the STATIC_URL

FULLCALENDAR_DEFAULTS = {
    'css_url': 'http://cdn.bootcss.com/fullcalendar/1.6.4/fullcalendar.css',
    'print_css_url': 'http://cdn.bootcss.com/fullcalendar/1.6.4/fullcalendar.print.css',
    'javascript_url': 'http://cdn.bootcss.com/fullcalendar/1.6.4/fullcalendar.min.js',
    'jquery_url': 'http://cdn.bootcss.com/jquery/2.1.4/jquery.min.js',
    'jquery_ui_url': 'http://cdn.bootcss.com/jqueryui/1.10.4/jquery-ui.js',
}

# Updates location based on configuration defined by 
# settings.py of the project

FULLCALENDAR = FULLCALENDAR_DEFAULTS.copy()
FULLCALENDAR.update(getattr(settings, 'FULLCALENDAR', {}))

def css_url():
    return FULLCALENDAR['css_url']

def print_css_url():
    return FULLCALENDAR['print_css_url']

def javascript_url():
    return FULLCALENDAR['javascript_url']

def jquery_url():
    return FULLCALENDAR['jquery_url']

def jquery_ui_url():
    return FULLCALENDAR['jquery_ui_url']
