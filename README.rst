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

And just use the mixin to keep track of a model:

.. code-block:: python

    from django_history.mixins import ModelDiffMixin


    class MyModel(ModelDiffMixin, models.Model):
        # ...


Features
--------

Get model tracking:

.. code-block:: python

    from django_history.models import ModelRegistry

    model_registry = ModelRegistry.get_registry_for_model(MyModel)

Following the previous snippet, we can track changes of a specific object

.. code-block:: python

    object_tracking = model_registry.filter(object_id=my_model.id)

Revert changes:

.. code-block:: python

    my_model = object_tracking.last().revert_change()

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
