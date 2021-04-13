#!/usr/bin/env python

"""Tests for `nldi_el_serv` package."""

import pytest

from click.testing import CliRunner

# from nldi_el_serv import nldi_el_serv
from nldi_el_serv import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    print(result)
    assert result.exit_code == 0
    assert 'xsatpoint' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '\n\nCommands:\n  xsatendpts\n' in help_result.output
