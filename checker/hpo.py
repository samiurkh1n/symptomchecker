"""HPO Library

Provides methods for querying the HPO API
"""

from dataclasses import dataclass
import json
from urllib.parse import quote
import requests
from typing import List

SEARCH_ENDPOINT_TEMPLATE = "https://hpo.jax.org/api/hpo/search/?q=%s"

@dataclass
class Hpo:
  name: str
  id: str

@dataclass
class HpoApiResponse:
  hpo: List[Hpo]
  status: int
  error_message: str

def get_hpo_id(query: str) -> HpoApiResponse:
  """ Returns
  - str : HPO ID. Empty if there is an error
  - int : 0 if okay, -1 if invalid parameter, -2 if internal error (e.g. API
    call failed)
  - str : error message. Empty if response is ok.
  """
  if len(query) == 0:
    return HpoApiResponse(
      hpo=[],
      status=-1,
      error_message=f"Invalid parameter. Got {query}. Want non-empty string")
  response = requests.get(SEARCH_ENDPOINT_TEMPLATE % quote(query))
  if response.status_code != 200:
    return HpoApiResponse(
      hpo=[],
      status=-2,
      error_message=f"Internal: API call returned {response.status_code}")
  query_result = HpoApiResponse(hpo=[], status=0, error_message="")
  hpo_data = json.loads(response.text)
  for term in hpo_data["terms"]:
    if (len(term["name"]) == 0) or (len(term["id"]) == 0):
      query_result.error_message = "Malformed response. Please retry"
      query_result.status = -2
      break
    query_result.hpo.append(Hpo(name=term["name"], id=term["id"]))
  return query_result
  