import textwrap

import locale
import click
import requests

from . import __version__, wikipedia

@click.command()
@click.version_option(version=__version__)
def main():
    """A Python project."""
    data = wikipedia.random_page()

    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
