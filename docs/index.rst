.. django-view-decorator documentation master file, created by
   sphinx-quickstart on Wed Mar 15 21:43:57 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to django-view-decorator's documentation!
=============================================


**django-view-decorator** is a Python library that allows you to define your view's url right next to your view's code.

URL routing in django is usually done in the `urls.py` file. This is fine for simple projects, but as your project grows, you will find yourself with a very large `urls.py` file. This is where **django-view-decorator** comes in. It allows you to define your view's url right next to your view's code.

See the :doc:`quickstart` for a quick introduction of how to use the decorator.


Inspiration
-----------

The decorator is very much inspired by the idea of "locality of behaviour" by Carson Gross (creator of HTMX): https://htmx.org/essays/locality-of-behaviour/.

It also bears resemblance to the `@app.route` decorator in Flask, the `@app.<HTTP method>` decorator in FastAPI and probably many other Python web frameworks.


.. toctree::
   :maxdepth: 1

   quickstart

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
