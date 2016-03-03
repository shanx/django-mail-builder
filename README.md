# django-mail-builder

Build EmailMessages easily from templates

## QuickStart

In your code, you can use the ``build_message`` function to build an ``EmailMessage`` class, sourcing its values from a template.

```
def build_message(template_names, extra_context=None, force_multipart=False,
                  **defaults):
```

Parameters:

template_names::
  A list of template names to select from.  A single template name will be converted to a list.

extra_context::
  Extra context to be passed when rendering blocks from the template.

force_multipart::
  Force use of ``EmailMultipartMessage`` instead of ``EmailMessage``.
  If a `html` block is provided then ``EmailMultipartMessage`` will be used anyway.

defaults::
  Default values to be passed to the message class.  These will be overidden by any template blocks.

## Template blocks

### Scalar fields:

These blocks will be rendered as is, and passed to the message.  If an 'html' block is passed, a ``EmailMultipartMessage`` will be constructed, and the `html` content will be added as a `text/html` alternative.

- subject
- from_email
- body
- html

### List fields:

These blocks will be rendered, and then split by lines using ``str.splitlines``.

- to
- bcc
- cc
- reply_to


# Views

A utility view is provided that extends ``django.views.generic.FormView`` to send an email on form valid.

```
from mail_builder.views import EmailFormView
```

Additional class properties:

- email_template
- fail_silently
