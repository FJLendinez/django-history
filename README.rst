=============================
Django History
=============================
.. image:: https://readthedocs.org/projects/django-history/badge/?version=latest
    :target: https://django-history.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://travis-ci.org/fjlendinez/django-history.svg?branch=master
    :target: https://travis-ci.org/fjlendinez/django-history

.. image:: https://codecov.io/gh/fjlendinez/django-history/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/fjlendinez/django-history

Small package to manage uploads and downloads in a centriliced way

Documentation
-------------

The full documentation is at https://django-history.readthedocs.io.

Quickstart
----------

Install Django History::

    pip install git+https://github.com/FJLendinez/django-history.git

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_history',
        ...
    )

Add Django History's URL patterns:

.. code-block:: python

    from django_history import urls as django_history_urls


    urlpatterns = [
        ...
        url(r'^', include(django_history_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
