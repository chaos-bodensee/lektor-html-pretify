 html-pretify
================
[![PyPI version](https://badge.fury.io/py/lektor-html-pretify.svg)](https://badge.fury.io/py/lektor-html-pretify)
 [![Downloads](https://pepy.tech/badge/lektor-html-pretify)](https://pepy.tech/project/lektor-html-pretify)
 ![Upload Python Package](https://github.com/chaos-bodensee/lektor-html-pretify/workflows/Upload%20Python%20Package/badge.svg)
 ![Linting Python package](https://github.com/chaos-bodensee/lektor-html-pretify/workflows/Linting%20Python%20package/badge.svg)

[Lektor](https://getlektor.com) plugin to pretify the HTML DOM using Beautiful Soup.

 How does it actually work?
----------------------------
 + It uses [Beautiful Soup](https://en.wikipedia.org/wiki/Beautiful_Soup_(HTML_parser)).
 + It looks for rendered ``.html`` files and pretify themi.

 Installation
-------------
You can install the plugin with Lektor's installer:
```bash
lektor plugins add lektor-html-pretify
```

Or by hand, adding the plugin to the packages section in your lektorproject file:
```ini
[packages]
lektor-html-pretify = 1.0.5
```
 Usage
------
To enable the plugin, pass the ``pretifyhtml`` flag when starting the development
server or when running a build:
```bash
# build and compile css from scss
lektor build -f pretifyhtml

# edit site with new generated css
lektor server -f pretifyhtml
```

 Python3
----------
It is highly recommended to use this plugin with a python3 version of lektor.

Since lektor can be used as a python module it is possible to enforce this *(after lektor is installed eg. with ``pip3 install --user --upgrade lektor``)* with the following command:
```bash
# run a python3 lektor server with new generated css
python3 -m lektor server -f pretifyhtml
```

 Development
-------------
To test and/or develop on this plugin in your running lektor installation, simply place it in the ``packages/`` Folder and have a look at the [Lektor Docs](https://www.getlektor.com/docs/plugins/dev/)

<!-- How to add to pypi: https://packaging.python.org/tutorials/packaging-projects/ -->
<!-- Python RELEASEING moved to github action -->
<!-- You have to edit the version number in README and setup.py manually -->

