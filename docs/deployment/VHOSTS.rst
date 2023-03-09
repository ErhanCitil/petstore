Apache + mod-wsgi configuration
===============================

An example Apache2 vhost configuration follows::

    WSGIDaemonProcess petstore-<target> threads=5 maximum-requests=1000 user=<user> group=staff
    WSGIRestrictStdout Off

    <VirtualHost *:80>
        ServerName my.domain.name

        ErrorLog "/srv/sites/petstore/log/apache2/error.log"
        CustomLog "/srv/sites/petstore/log/apache2/access.log" common

        WSGIProcessGroup petstore-<target>

        Alias /media "/srv/sites/petstore/media/"
        Alias /static "/srv/sites/petstore/static/"

        WSGIScriptAlias / "/srv/sites/petstore/src/petstore/wsgi/wsgi_<target>.py"
    </VirtualHost>


Nginx + uwsgi + supervisor configuration
========================================

Supervisor/uwsgi:
-----------------

.. code::

    [program:uwsgi-petstore-<target>]
    user = <user>
    command = /srv/sites/petstore/env/bin/uwsgi --socket 127.0.0.1:8001 --wsgi-file /srv/sites/petstore/src/petstore/wsgi/wsgi_<target>.py
    home = /srv/sites/petstore/env
    master = true
    processes = 8
    harakiri = 600
    autostart = true
    autorestart = true
    stderr_logfile = /srv/sites/petstore/log/uwsgi_err.log
    stdout_logfile = /srv/sites/petstore/log/uwsgi_out.log
    stopsignal = QUIT

Nginx
-----

.. code::

    upstream django_petstore_<target> {
      ip_hash;
      server 127.0.0.1:8001;
    }

    server {
      listen :80;
      server_name  my.domain.name;

      access_log /srv/sites/petstore/log/nginx-access.log;
      error_log /srv/sites/petstore/log/nginx-error.log;

      location /500.html {
        root /srv/sites/petstore/src/petstore/templates/;
      }
      error_page 500 502 503 504 /500.html;

      location /static/ {
        alias /srv/sites/petstore/static/;
        expires 30d;
      }

      location /media/ {
        alias /srv/sites/petstore/media/;
        expires 30d;
      }

      location / {
        uwsgi_pass django_petstore_<target>;
      }
    }
