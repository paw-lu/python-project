import textwrap

import locale
import click
import requests

from . import __version__

location_info = locale.getlocale()[0]
if location_info is not None:
    country = location_info.split("_")[0]
else:
    country = "en"
API_URL = f"https://{country}.wikipedia.org/api/rest_v1/page/random/summary"

@click.command()
@click.version_option(version=__version__)
def main():
    """A Python project."""
    try:
        with requests.get(API_URL) as responce:
            responce.raise_for_status()
            data = responce.json()
            title = data["title"]
            extract = data["extract"]
            click.secho(title, fg="green")
            click.echo(textwrap.fill(extract))
    except requests.RequestException as error:
        click.secho(textwrap.fill(str(error)), fg="red")



