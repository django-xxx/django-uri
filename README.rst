==========
django-uri
==========

Components of an URI
====================

![](http://ww4.sinaimg.cn/large/c05783a7gw1f2h380qt9jj21500i8q5o.jpg)

* [Components of an URI](https://medialize.github.io/URI.js/about-uris.html)

Installation
============

::

    pip install django-uri


Usage
=====

::

    request.uri.origin
    request.uri.scheme


Settings.py
===========

::

    # Use `MIDDLEWARE_CLASSES` prior to Django 1.10
    MIDDLEWARE = (
        ...
        'uri.middleware.URIMiddleware',
        ...
    )

