# Django View Decorator

[![Tests](https://github.com/valberg/django-view-decorator/actions/workflows/test.yml/badge.svg)](https://github.com/valberg/django-view-decorator/actions/workflows/test.yml)
[![Documentation](https://readthedocs.org/projects/django-view-decorator/badge/?version=latest)](https://django-view-decorator.readthedocs.io/en/latest/?badge=latest)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/valberg/django-view-decorator/main.svg)](https://results.pre-commit.ci/latest/github/valberg/django-view-decorator/main)
[![PyPI - Version](https://img.shields.io/pypi/v/django-view-decorator.svg)](https://pypi.org/project/django-view-decorator)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-view-decorator.svg)](https://pypi.org/project/django-view-decorator)

-----

**django-view-decorator** is decorator aimed at bringing locality of behaviour to the connection between a URL and a view in Django.

Read more about the motivation behind the package in a recent [blogpost](https://valberg.dk/bringing-locality-of-behaviour-to-django-views-and-urls.html).



**Table of Contents**

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

```console
pip install django-view-decorator
```

## Usage

Setup the project URLconf to include URLs from django-view-decorator:

```python
# project/urls.py (this is what we point the ROOT_URLCONF setting at)
from django.urls import path

from django_view_decorator import include_view_urls

urlpatterns = [
    path("", include_view_urls()),
]
```

Use the decorator like so, for:

### Function-based views

```python
# foos/views.py
from django_view_decorator import view

@view(paths="/foo/", name="foo")
def foo(request: HttpRequest) -> HttpResponse:
    return HttpResponse("foo")
```

### Class-based views
```python
@view(paths="/foo/", name="foo-list")
class FooList(ListView):
    model = Foo
```

### Parameters

* `paths`: is in a plural form because support also a list of paths
* `name` the classic route name
* `namespace`: {I don't know what to write here}
* `extra_modules`: can be a real path or the python module itselfs (require a list)
* `login_required`: so you can avoid the Django decorator
* `permission_required`: so you can avoid the Django decorator

### entra_modules example for real paths

```
import os
# We need the project directory
root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
urlpatterns = [
    path("", include_view_urls(extra_modules=[root + "/portal/views"])),
]
```

## Development

```console
git clone
cd django-view-decorator
pip install hatch
hatch run tests:cov
hatch run tests:typecheck
```

## License

`django-view-decorator` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
