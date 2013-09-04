# Tumblr.com Blog Proxy

A Python based WSGI application to proxy request to the [Tumblr.com](http://www.tumblr.com/) API. Supports:

* hosting of a Tumblr blog using a subdirectory**
* custom rendering using [Jinja2](http://jinja.pocoo.org/docs/) templates
* logging

** Requires [nginx](http://wiki.nginx.org/HttpProxyModule) or a similar reverse proxy configuration (see blow).


## Overview

* tumblrproxy/templates/blog : templates to customize blog layout

* tumblrproxy/controllers/blog : application logic

    * controllers/blog/__init__.py : URL routing

    * controllers/blog/view.py : view rendering logic

* tumblrproxy/__init__.py : WSGI application


## Installation

Get latest code copy:

    git clone https://github.com/140am/tumblrproxy
    cd tumblrproxy

Using a virtualenv setup (optionally but recommended):

    virtualenv env
    source env/bin/activate

Setup the project environment and database:

    python setup.py develop

Start the development web server:

    pserve development.ini --reload

Update the `development.ini` file with your [Tumblr Application](http://www.tumblr.com/oauth/apps) settings:

    tumblr.blog = TUMBLR_USERNAME
    tumblr.consumer_key =
    tumblr.consumer_secret =

### nginx Sample Configuration

    server {
        listen 80;
        server_name www.yoursite.tld;

        location ~ ^/blog/?(.*)$ {
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            if (!-f $request_filename) {
                proxy_pass http://127.0.0.1:6543/$1;
            }
            proxy_connect_timeout 60;
        }

        root /www/yoursite.tld;
    }


## MIT License

> Copyright (c) 2013 Manuel Kreutz
> 
> Permission is hereby granted, free of charge, to any person
> obtaining a copy of this software and associated documentation files
> (the "Software"), to deal in the Software without restriction,
> including without limitation the rights to use, copy, modify, merge,
> publish, distribute, sublicense, and/or sell copies of the Software,
> and to permit persons to whom the Software is furnished to do so,
> subject to the following conditions: 
>
> The above copyright notice and this permission notice shall be
> included in all copies or substantial portions of the Software. 
> 
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
> EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
> MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
> NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
> BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
> ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
> CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.