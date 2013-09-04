import logging
import urlparse
import oauth2
import pytumblr

from pyramid.view import view_config, notfound_view_config

from tumblrproxy.lib.template_filter import root_path

logging.basicConfig(level = logging.DEBUG)
log = logging.getLogger(__name__)


def get_oauth_client(request):

    REQUEST_TOKEN_URL = 'http://www.tumblr.com/oauth/request_token'

    consumer = oauth2.Consumer(
        request.registry.settings['tumblr.consumer_key'],
        request.registry.settings['tumblr.consumer_secret']
    )
    client = oauth2.Client(consumer)

    resp, content = client.request(REQUEST_TOKEN_URL, "GET")

    request_token = dict(urlparse.parse_qsl(content))
    OAUTH_TOKEN = request_token['oauth_token']
    OAUTH_TOKEN_SECRET = request_token['oauth_token_secret']

    client = pytumblr.TumblrRestClient(
        request.registry.settings['tumblr.consumer_key'],
        request.registry.settings['tumblr.consumer_secret'],
        OAUTH_TOKEN,
        OAUTH_TOKEN_SECRET
    )

    return client


@view_config(route_name='post_list', renderer='blog/list.jinja2', request_method='GET')
@view_config(route_name='post_list_tag', renderer='blog/list.jinja2', request_method='GET')
def post_list(request):

    client = get_oauth_client(request)

    if request.matchdict.get('tag_name'):
        post_objs = client.posts(
            request.registry.settings['tumblr.blog'],
            tag=request.matchdict.get('tag_name'),
            offset=0,
            limit=10
        )
    else:
        post_objs = client.posts(
            request.registry.settings['tumblr.blog'],
            offset=0,
            limit=10
        )

    return {
        'root_path' : root_path(request),
        'tag_name' : request.matchdict.get('tag_name'),
        'post_objs' : post_objs
    }


@view_config(route_name='post_view', renderer='blog/list.jinja2', request_method='GET')
def post_view(request):

    client = get_oauth_client(request)

    post_objs = client.posts(
        request.registry.settings['tumblr.blog'],
        id=int(request.matchdict.get('post_id'))
    )

    return {
        'root_path' : root_path(request),
        'post_objs' : post_objs
    }


@notfound_view_config(renderer='json')
def not_found_error(request):
    request.response.status = 404

    return {'error' : {
        'code' : 404,
        'message' : 'Ooops. Invalid request.'
    }}
