# -*- coding: utf-8 -*-


def repalce_uri_parts(request, new, olds=[]):
    if not isinstance(olds, list):
        olds = [olds]
    url = request.build_absolute_uri()
    for old in olds:
        url = url.replace(old, new)
    return url
