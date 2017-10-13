# xplor
Python package to perform exploratory data analysis

A ton of credit is due to @ritikabhasker, whose [Intro to EDA](https://github.com/ritikabhasker/Intro-to-EDA) lecture  provided the inspiration, and the foundation for this effort.

Change Log:
- 10/8/2017
	- Updated original code to python3
- 10/10/2017
	- Reformatted output, updated the describe to include unique values @Dale Wahl
	- Feature dropped, but @Dale Wahl is still cool
- 10/11/2017
	- Added feature plotting, and switched up the output format
	- Added assert, type coercion coming soon
- 10/13/2017
	- Moved to class model
	- Added support for pandas series

Installation:

Running the set up:

Go to the directory and enter the following:

If you are using macOS:
```commandline
python3.6 setup.py bdist_egg
```

_Note: The version number for python might differ for your system_

For Windows:
```commandline
python setup.py bdist_egg
```

After building this you will need to install locally:

```commandline
easy_install dist/xplor-0.1-py3.6.egg `#0.1 corresponds to the version number`
```


To test this, open python3 in either Terminal or Command Prompt, and try importing `xplor` with:

```python
import xplor
```

If there are no error messages, the build was successful.
You can now access mTree as you would any other python package.
