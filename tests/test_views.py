
from django.test import TestCase


class ViewTestCase(TestCase):

    def test_view(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
