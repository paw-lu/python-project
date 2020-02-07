import textwrap

import locale
import click
import requests

from . import __version__

country = locale.getlocale()[0].split("_")[0]
# API_URL = f"https://{country}.wikipedia.org/api/rest_v1/page/random/summary"
API_URL = f"https://{country}.wikipedia.org/api/rest_v1/pagy"

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



