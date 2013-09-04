import logging

from tumblrproxy.controllers.blog import view

logging.basicConfig(level = logging.DEBUG)
log = logging.getLogger(__name__)


def includeme(config):

    config.add_route('post_list', '/')
    config.add_route('post_view', '/{post_id:\d+}-{post_title}')
    config.add_route('post_list_tag', '/category/{tag_name:\w+}')

    config.scan()
