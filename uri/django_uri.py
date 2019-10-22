# -*- coding: utf-8 -*-


def repalce_uri_parts(request, new, olds=[]):
    if not isinstance(olds, list):
        olds = [olds]
    new_url = old_url = request.build_absolute_uri()
    for old in olds:
        new_url = new_url.replace(old, new)
    return new_url, new_url != old_url
