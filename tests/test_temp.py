from click.testing import CliRunner
# import pytest

# from nldi_el_serv import nldi_el_serv
from nldi_el_serv import cli
# import nldi_el_serv
from tempfile import NamedTemporaryFile
import json

runner = CliRunner()
print(runner.invoke(cli.main))

# result = runner.invoke(cli.main, ['xsatendpts', '--help'])
# print(result.output)
# help_result = runner.invoke(cli.main, ['--help'])
# print(help_result.output)
# help_result2 = runner.invoke(cli.XSAtEndPts, ['--help'])
# print(help_result2.output)
with NamedTemporaryFile(mode='w+') as tf:
    help_result3a = runner.invoke(
                                    cli.main,
                                    [
                                        'xsatpoint', '-f', tf.name,
                                        '--lonlat', '-103.80119', '40.2684',
                                        '--width', '100', '--numpoints', '11'
                                    ]
                                  )
    assert(help_result3a.exit_code == 0)
    ogdata = json.load(tf)
    feat = ogdata.get('features')
    print(len(feat))
    assert(len(feat) == 11)
    print(ogdata)

help_result3 = runner.invoke(cli.main, ['xsatpoint', '--lonlat', '-103.80119', '40.2684',
                                        '--width', '100', '--numpoints', '11'])

print(help_result3.output)
tmp = 0
