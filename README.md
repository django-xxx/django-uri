# django-uri
Django URI

## [Components of an URI](https://medialize.github.io/URI.js/about-uris.html)
![](http://ww4.sinaimg.cn/large/c05783a7gw1f2h380qt9jj21500i8q5o.jpg)

## Installation
```shell
pip install django-uri
```

## Usage
```python
request.uri.origin
request.uri.scheme
```

## Settings.py
```python
# Use `MIDDLEWARE_CLASSES` prior to Django 1.10
MIDDLEWARE = (
    ...
    'uri.middleware.URIMiddleware',
    ...
)
```
