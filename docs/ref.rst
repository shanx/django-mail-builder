Reference
---------

.. py:module:: mail_builder

.. py:function:: build_message(template_names, extra_context=None, force_multipart=False, **defaults)

   Constructs a ``EmailMessage`` using the template to provide arguments.

   :param sequence template_names: A list of template names to pass to ``select_template``.  If a single string is passed, it will be wrapped in a list
   :param dict extra_context: Extra context to pass to the template blocks.
   :param bool force_multipart: Ensure a ``EmailMultipartMessage`` is built, even when no `hmtl` content is provided.
   :param varied defaults: All extra arguments will be passed to the ``EmailMessage``
   :return: ``EmailMessage`` instance.


.. py:module:: mail_builder.views


.. py:class:: EmailFormView

   A sub-class of ``FormView`` which renders and sends an email on form valid.

   .. py:attribute:: email_template

      The value to pass as `email_templates` to `build_message`

   .. py:attribute:: fail_silently

      (Default: True)

      Passed to ``EmailMessage.send``

   .. py:attribute:: email_kwargs

      (Default: {})

      Arguments to pass when calling `build_message`

   .. py:method:: get_email_context(form, **kwargs)

      Hook to build the context to be used when rendering email template blocks.
      The default implementation will return ``kwargs``, after setting 'form' to the form's ``cleaned_data``, if it's not set.

   .. py:method:: get_email_kwargs(form, **kwargs)

      Builds the dict of keyword arguments to pass to `build_message`.

      The default implementation updates `kwargs` from ``self.email_kwargs``.

   .. py:method:: form_valid(form)

      Calls `self.get_email_context` and `self.get_email_kwargs`, then builds a message using `build_message`.
      Then calls ``send(fail_silently=self.fail_silently)`` on the message.
      Finally calls the superclass's ``form_valid`` method.
