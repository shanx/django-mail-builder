
from django.test import TestCase


from mail_builder import build_message


class BuilderTestCase(TestCase):

    def test_empty(self):
        msg = build_message('empty.email')
        self.assertEqual(msg.to, [])

    def test_defaults(self):
        msg = build_message('empty.email', from_email='test@test.com')
        self.assertEqual(msg.to, [])
        self.assertEqual(msg.from_email, 'test@test.com')

    def test_subject(self):
        msg = build_message('subject.email')
        self.assertEqual(msg.subject, 'Test Subject')
