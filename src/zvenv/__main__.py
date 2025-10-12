'''This simple utility provides simple user interactable venv creation or modification with automatic dependency installation.

This is meant to be a one command solution for creating venvs containing packages to reduce barrier of entry. 

Usage examples:
python3 -m zvenv create 
python3 -m zvenv create ~/Projects/PythonProject
python3 -m zvenv remove
python3 -m zvenv remove ~/Projects/PythonProject

Once you have a venv installed, refer to https://docs.python.org/3/library/venv.html#how-venvs-work on how to activate a virtual environment.

Created by Zechariah Boyer'''
import argparse
from shutil import rmtree
from pathlib import Path
from .ebpkgs import EnvBuilderPkgs

def exit_message(text : str):
    '''Gives basic text output on exit to be more informative.'''
    print(text)
    exit()

if __name__ != '__main__':
    exit_message('This script cannot be imported!')

LINES = str(__doc__).splitlines(True)

parser = argparse.ArgumentParser(
    prog = 'zvenv',
    description = ''.join(LINES[:1]),
    epilog = ''.join(LINES[2:]),
    formatter_class=argparse.RawDescriptionHelpFormatter
)
parser.add_argument(
    'task', choices = ('create','update','remove'),
    help = 'Tells script what task to do.'
)
parser.add_argument(
    'dir', nargs = '?', default = Path.cwd(),
    help = 'Path to the directory where a venv will be made. Not providing a path will always default to current working directory. The directory must contain a requirements.txt file. (default: %(default)s)'
)

args = parser.parse_args()
pdir = Path(args.dir)
venv = pdir / 'venv'

def create():
    '''Create method'''
    print('You will create a venv located at ' + str(pdir))
    res = input('Are you sure about this? (Y)es/No: ').lower()
    if res != '' and res not in ('y','yes'):
        exit_message('Creation canceled.')
    EnvBuilderPkgs(
        clear = True, symlinks = False, upgrade = False, with_pip = True, upgrade_deps = False, system_site_packages = True,
        requirements = pdir / 'requirements.txt'
    ).create(venv)

def update():
    '''Update method'''
    if venv.is_dir():
        print('You will update a venv located at ' + str(venv))
        res = input('Are you sure about this? (Y)es/No: ')
        if res != '' and res not in ('y','yes'):
            exit_message('Update canceled.')
        EnvBuilderPkgs(
            clear = False, symlinks = False, upgrade = True, with_pip = True, upgrade_deps = True, system_site_packages = True,
            requirements = pdir / 'requirements.txt'
        ).create(venv)
    else:
        exit_message('venv does not exist!')

def remove():
    '''Remove method'''
    if venv.is_dir():
        print('You will remove a venv located at ' + str(venv))
        res = input('Are you sure about this? (Y)es/No: ')
        if res != '' and res not in ('y','yes'):
            exit_message('Removal canceled.')
        rmtree(str(venv), ignore_errors = False)
    else:
        exit_message('venv does not exist!')

match args.task:
    case 'create':
        create()
    case 'update':
        update()
    case 'remove':
        remove()
