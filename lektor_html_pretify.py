#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin


class HtmlPretifyPlugin(Plugin):
    name = 'html-pretify'
    description = u'Lektor Plugin to pretify your HTML Dome'

    def on_process_template_context(self, context, **extra):
        def test_function():
            return 'Value from plugin %s' % self.name
        context['test_function'] = test_function
