# -*- coding: utf-8 -*-

from django_six import MiddlewareMixin
from six.moves import urllib_parse


class DotDict(dict):
    """ dot.notation access to dictionary attributes """
    def __getattr__(self, attr):
        return self.get(attr)
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class URIMiddleware(MiddlewareMixin):

    def process_request(self, request):
        parts = urllib_parse.urlparse(request.build_absolute_uri())
        parts = parts._replace(path='', params='', query='', fragment='')
        request.uri = DotDict({
            'origin': urllib_parse.urlunparse(parts),  # or parts.geturl()
            'scheme': 'https' if request.is_secure() else 'http',
        })
        return None
