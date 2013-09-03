from pyramid.config import Configurator
from jinja2.utils import import_string


def main(global_config, **settings):
    """ This function returns the Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    # http://docs.pylonsproject.org/projects/pyramid_exclog/dev/api.html#pyramid_exclog.includeme
    config.include('pyramid_exclog')
    # https://docs.pylonsproject.org/projects/pyramid_jinja2/dev/api.html#pyramid_jinja2.includeme
    config.include('pyramid_jinja2')
    config.get_jinja2_environment().filters.update({
        'date_format' : import_string('tumblrproxy.lib.template_filter.date_format'),
    })

    # view handler
    config.include('tumblrproxy.controllers.blog')

    # jinja2 configuration
    config.add_jinja2_search_path("tumblrproxy:templates")

    # static content route
    config.add_static_view('static', 'static', cache_max_age=3600)

    return config.make_wsgi_app()
