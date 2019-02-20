# HTML Tags

![](djangocms_html_tags.jpg)

## Installation

Add `djangocms_html_tags` to **INSTALLED_APPS**:

```python
INSTALLED_APPS = [
    ...
    "djangocms_html_tags",
    ...
]
``` 

Run migrations:

```shell
$ python manage.py migrate
```

## Contribution

Using Docker & Dosh scripts:

```shell
$ dosh runtests  # to run the unit tests and see the coverage report.
$ dosh shell  # to use Django shell or Python REPL in the development.
```

If you don't use Docker, you can try Virtualenv instead:

```shell
$ python -m pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate  # or run activate.ps1 if you use PowerShell.
$ (venv) python -m pip install -r demo/requirements.txt
$ (venv) python setup.py test
```
