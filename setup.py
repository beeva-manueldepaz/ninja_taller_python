from distutils.core import setup
from os.path import join,dirname

with open(join(dirname(__file__), 'requirements.txt')) as f:
    required = f.read().splitlines()

setup(
    name='ninja_taller',
    description='Learning Python :)',
    install_requires=required,
    version='0.0.1',
    packages=['02_web.tests'],
    url='https://github.com/beeva-manueldepaz/ninja_taller_python',
    license='MIT',
    author='Manuel E. de Paz Carmona',
)
