from django.test import Client, TestCase

class HomeTestCase(TestCase):
  def test_home_returns_ok(self):
    c = Client()
    got = c.get('/')
    self.assertEqual(got.status_code, 200)