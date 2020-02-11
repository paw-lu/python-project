from dataclasses import dataclass

import click
import desert
import marshmallow
import requests


@dataclass
class Page:
    title: str
    extract: str


# Tell Marshmallow to ignore unknown fields via meta
schema = desert.schema(Page, meta={"unknown": marshmallow.EXCLUDE})

API_URL = "https://{language}.wikipedia.org/api/rest_v1/page/random/summary"


def random_page(language: str = "en") -> Page:  # JSON hard to express as typ3
    url = API_URL.format(language=language)
    try:
        with requests.get(url) as response:
            response.raise_for_status()
            data = response.json()
            return schema.load(data)
    except (requests.RequestException, marshmallow.ValidationError) as error:
        message = str(error)
        raise click.ClickException(message)
