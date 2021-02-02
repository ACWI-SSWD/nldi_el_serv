"""Console script for nldi_el_serv."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for nldi_el_serv."""
    click.echo("Replace this message by putting your code into "
               "nldi_el_serv.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
