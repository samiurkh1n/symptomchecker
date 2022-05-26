from checker import hpo

import json
from django.test import TestCase
from unittest import mock

sample_query = 'Prominent supraorbital'

sample_query_response = {
  "terms" : [
    {
      "name": "Prominent supraorbital ridges",
      "id": "HP:0000336"
    },
    {
      "name": "Prominent supraorbital arches in adult",
      "id": "HP:0004676"
    }
  ],
}

def mocked_request_get(*args, **kwargs):
  class MockResponse:
    def __init__(self, data: str, status: int):
      self.text = data
      self.status_code = status

  if args[0] == 'https://hpo.jax.org/api/hpo/search/?q=Prominent%20supraorbital':
    return MockResponse(data=json.dumps(sample_query_response), status=200)
  return MockResponse(data="", status=500)


class HpoTest(TestCase):
  def test_return_invalid_argument_on_empty_query(self):
    self.assertEqual(hpo.get_hpo_id("").status, -1)

  @mock.patch('requests.get', side_effect=mocked_request_get)
  def test_return_internal_error_on(self, mocked):
    self.assertEqual(hpo.get_hpo_id("trigger internal error").status, -2)

  @mock.patch('requests.get', side_effect=mocked_request_get)
  def test_query_returns_hpo(self, mocked):
    response = hpo.get_hpo_id(sample_query)
    want = [
      hpo.Hpo(name="Prominent supraorbital ridges", id="HP:0000336"),
      hpo.Hpo(name="Prominent supraorbital arches in adult", id="HP:0004676"),
    ]
    self.assertEqual(response.status, 0)
    self.assertCountEqual(response.hpo, want)

  