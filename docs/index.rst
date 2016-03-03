.. Django Mail Builder documentation master file, created by
   sphinx-quickstart on Thu Mar  3 18:36:44 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Django Mail Builder
===================

Build email messages from templates.

Contents:

.. toctree::
   :maxdepth: 2

   overview
   templates
   ref

Quick Start
-----------

1. Install the package

   .. code-block:: sh

      $ pip install django-mail-builder

2. Write a template

   .. code-block:: html
      :name: email/welcome.email

      {% block subject %}Thanks for signing up to Awesome Site!{% endblock %}
      {% block to %}{{ user.email }}{% endblock %}
      {% block body %}
      Thanks for joining our site!

      We hope you love how awesome it is!
      {% endblock %}
      {% block html %}
      <h1> Thanks for joining our site! </h1>

      <p> We hope you love how awesome it is!
      {% endblock %}


3. In your view, build the message and send it.

   .. code-block:: python

      msg = build_message('email/welcome.email', {'user': request.user})
      msg.send()


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

