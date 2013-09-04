import datetime

def date_format(date_s, format=None):
    if not format:  # default formating
        format = '%m/%d/%Y'
    if not date_s: return '-'
    if isinstance(date_s, str) or isinstance(date_s, unicode):  # parse a string
        try:
            date_obj = datetime.datetime.strptime(date_s, '%Y-%m-%d %H:%M:%S %Z')
        except ValueError: return
        date_obj = date_obj.strftime(format)
    else:  # parse a date object
        date_obj = date_s

    return date_obj

def root_path(request):
    if request.registry.settings.get('tumblr.root'):
        path = request.registry.settings.get('tumblr.root')
    else:
        path = request.path_info
    if not path == '/':
        return '%s/' % path
    else:
        return path
