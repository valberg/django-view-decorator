# Django View Decorator

[![Tests](https://github.com/valberg/django-view-decorator/actions/workflows/test.yml/badge.svg)](https://github.com/valberg/django-view-decorator/actions/workflows/test.yml)
[![Documentation](https://readthedocs.org/projects/django-view-decorator/badge/?version=latest)](https://django-view-decorator.readthedocs.io/en/latest/?badge=latest)
[![PyPI - Version](https://img.shields.io/pypi/v/django-view-decorator.svg)](https://pypi.org/project/django-view-decorator)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-view-decorator.svg)](https://pypi.org/project/django-view-decorator)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/valberg/django-view-decorator/main.svg)](https://results.pre-commit.ci/latest/github/valberg/django-view-decorator/main)

-----

**django-view-decorator** is decorator aimed at bringing locality of behaviour to the connection between a URL and a view in Django.



**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install django-view-decorator
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
