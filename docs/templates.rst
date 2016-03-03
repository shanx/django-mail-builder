Templates
---------

Templates are used to supply blocks, which are rendered to provide values to be
passed to the ``EmailMessage`` constructor.

Blocks
======

The following blocks are used:

- subject
- from_email
- body
- html
- to
- cc
- bcc
- reply_to

For the meaning of these fields (except ``html``), see the `EmailMessage` docs.

All values are stripped, and the email address fields (`to`, `cc`, `bcc`, and
`reply_to`) are split on newlines into a list, then stripped.
