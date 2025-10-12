# Zvenv
This is a utility I made specificially to make setting up a venv easier. Venv creation is handled for you if you install zvenv.
Run `python3 -m zvenv --help` for more information.

**Be aware that you require venv.** On Linux, install it through your package manager if it is missing.

## Pypi
It is not yet available on pypi.

## Release
Download a release file. Locate either the .whl or .tar.gz file.
```bash
pip install --user PASTE_ITS_PATH_HERE
```

## Source code
Pull it from https://github.com/ZechariahB/zvenv.git

You may require build.
```bash
pip install --upgrade build
```
No pip with dnf *(Fedora)*
```bash
sudo dnf install python3-build
```

Installing with pip will automatically attempt to build a package and install it if possible. `-e` allows the source code to be easily editable.
```bash
pip install --user -e PASTE_PATH_TO_ZVENV_HERE
```

Go into the directory of this project. Once you make final changes, you can build a package to distribute.
```bash
python3 -m build
```
