Overview
--------

The ``EmailMessage
(https://docs.djangoproject.com/en/1.9/topics/email/#the-emailmessage-class)`` class in Django accepts a number of arguments, and when
you're sending emails from your app, you need to supply them.  Sometimes this
is simple, as the values are fixed (i.e. from_email), whilst others are more
dynamic (such as the message body).

One way or another you need to produce these values and pass them to the class.

And sometimes you want ``EmailMultipartMessage`` instead, for instane when you
want to send plain text _and_ html.

The ``build_message`` function helps you do this by letting you pass arguments,
as well as use blocks from a template to render others.


The Arguments
=============

As shown in the Django docs, the ``EmailMessage`` class takes the following
arguments:

- subject
- body
- from_email
- to
- bcc
- connection
- attachments
- headers
- cc
- reply_to

The ``build_message`` function will accept and and all of them as keyword
arguments, but will also try to render any blocks with those names from the
provided template and update the values from there.

Any mix of keyword and template supplied arguments is valid, as long as there
are enough to satisfy the ``EmailMessage`` class.

The unsent message instance is returned, so you can update fields, override
them, add attachments or headers, or anything else you like before sending.
