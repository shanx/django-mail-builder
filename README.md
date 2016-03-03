# django-mail-builder

Build EmailMessages easily from templates

## QuickStart

In your code, you can use the ``build_message`` function to build an ``EmailMessage`` class, sourcing its values from a template.

```
def build_message(template_names, extra_context=None, force_multipart=False,
                  **defaults):
```

Pass a template name (or list of names), and blocks from that template will be used to fill the properties of the message.

Scalar fields:

- subject
- from_email
- body
- html

These blocks will be rendered as is, and passed to the message.  If an 'html' block is passed, a ``EmailMultipartMessage`` will be constructed, and the `html` content will be added as a `text/html` part.
