'''This simple module allows automatic installation of packages.

Created by Zechariah Boyer'''
from venv import EnvBuilder
from pathlib import Path
from subprocess import run

class EnvBuilderPkgs(EnvBuilder):
    '''This extends EnvBuilder from venv. An OS shell command is ran to achieve PIP package installation. This is the official supported method for PIP unfortunate as it is.'''

    def __init__(self, *args, requirements: Path, **kwargs):
        if isinstance(requirements, Path):
            if not requirements.is_file():
                raise FileNotFoundError('requirements file does not exist!')
        else:
            raise TypeError('requirements be either an instance of list or PurePath')

        self.requirements = requirements
        super().__init__(*args, **kwargs)

    def post_setup(self, context):
        run(
            [context.env_exe, '-m', 'pip', 'install', '-r', str(self.requirements)],
            check = True
        )
