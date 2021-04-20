from click.testing import CliRunner
# import pytest

# from nldi_el_serv import nldi_el_serv
from nldi_el_serv import cli
# import nldi_el_serv

runner = CliRunner()
print(runner.invoke(cli.main))

# result = runner.invoke(cli.main, ['xsatendpts', '--help'])
# print(result.output)
# help_result = runner.invoke(cli.main, ['--help'])
# print(help_result.output)
# help_result2 = runner.invoke(cli.XSAtEndPts, ['--help'])
# print(help_result2.output)
# help_result3 = runner.invoke(cli.main, ['xsatpoint', '-f', 'test1.json',
#                                         '--lonlat', '-103.80119', '40.2684',
#                                         '--width', '1000', '--numpoints', '101'])
help_result3 = runner.invoke(cli.main, ['xsatpoint', '--lonlat', '-103.80119', '40.2684',
                                        '--width', '1000', '--numpoints', '101'])

print(help_result3.output)
tmp = 0
