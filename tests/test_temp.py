from click.testing import CliRunner

# from nldi_el_serv import nldi_el_serv
from nldi_el_serv import cli

runner = CliRunner()
print(runner.invoke(cli.main))

result = runner.invoke(cli.main)
print(result.output)
help_result = runner.invoke(cli.main, ['--help'])
print(help_result.output)
tmp = 0
