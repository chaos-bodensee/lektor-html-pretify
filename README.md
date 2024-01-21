 html-pretify
================
[![PyPI version](https://badge.fury.io/py/lektor-html-pretify.svg)](https://badge.fury.io/py/lektor-html-pretify)
 [![Downloads](https://pepy.tech/badge/lektor-html-pretify)](https://pepy.tech/project/lektor-html-pretify)
 [![Linting Python package](https://github.com/chaos-bodensee/lektor-html-pretify/actions/workflows/pythonpackage.yml/badge.svg)](https://github.com/chaos-bodensee/lektor-html-pretify/actions/workflows/pythonpackage.yml)
 [![Yamllint GitHub Actions](https://github.com/chaos-bodensee/lektor-html-pretify/actions/workflows/yamllint.yaml/badge.svg)](https://github.com/chaos-bodensee/lektor-html-pretify/actions/workflows/yamllint.yaml)

[Lektor](https://getlektor.com) plugin to pretify the HTML DOM using Beautiful Soup.

 How does it actually work?
----------------------------
 + It uses [Beautiful Soup](https://en.wikipedia.org/wiki/Beautiful_Soup_(HTML_parser)).
 + It looks for rendered ``.html`` files and pipe it through Beautiful Soup, after opening the files via [codecs](https://docs.python.org/3/library/codecs.html).

 Installation
-------------
You can install the plugin with Lektor's installer:
```bash
lektor plugins add lektor-html-pretify
```

Or by hand, adding the plugin to the packages section in your lektorproject file:
```ini
[packages]
lektor-html-pretify = 2.0.0
```

 Python3
----------
It is highly recommended to use this plugin with a python3 version of lektor.

Since lektor can be used as a python module it is possible to enforce this *(after lektor is installed eg. with ``pip3 install --user --upgrade lektor``)* with the following command:
```bash
# run a python3 lektor server
python3 -m lektor server
```

 Development
-------------
To test and/or develop on this plugin in your running lektor installation, simply place it in the ``packages/`` Folder and have a look at the [Lektor Docs](https://www.getlektor.com/docs/plugins/dev/)

<!-- How to add to pypi: https://packaging.python.org/tutorials/packaging-projects/ -->
<!-- Python RELEASEING moved to github action -->
<!-- You have to edit the version number in README and setup.py manually -->
