#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# find and open html files
import os

# pretify file
import codecs
import chardet
from bs4 import BeautifulSoup

# general Lektor plugins
from lektor.pluginsystem import Plugin
from lektor.reporter import reporter

class HtmlPretifyPlugin(Plugin):
    name = 'html-pretify'
    description = u'Lektor Plugin to pretify your HTML DOM using BeautifulSoup'

    def is_enabled(self, build_flags):
        return bool(build_flags.get('pretifyhtml'))

    def find_html_files(self, destination):
        """
        Finds all html files in the given destination.
        """
        for root, dirs, files in os.walk(destination):
            for f in files:
                if f.endswith('.html'):
                    yield os.path.join(root, f)

    def pretify_file(self, target):
        """
        Minifies the target html file.
        """
        html = open(target, 'rb')
        enc = chardet.detect(html.read())['encoding']
        html.close()
        with codecs.open(target, 'r+', enc) as f:
            result = BeautifulSoup(f.read(), 'html.parser')
            f.seek(0)
            f.write( result.prettify(formatter="html") )
            f.truncate()

    def on_after_build_all(self, builder, **extra):
        """
        after-build-all lektor event
        """
        try:
            is_enabled = self.is_enabled(builder.build_flags)
        except AttributeError:
            is_enabled = self.is_enabled(builder.extra_flags)

        if not is_enabled:
            return

        reporter.report_generic('HTML minification started')
        for htmlfile in self.find_html_files(builder.destination_path):
            self.pretify_file(htmlfile)
        reporter.report_generic('HTML minification finished')
