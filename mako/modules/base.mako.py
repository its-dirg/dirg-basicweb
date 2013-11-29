# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1385733002.447296
_enable_loop = True
_template_filename = u'/opt/dirg/dirg-util/mako/templates/base.mako'
_template_uri = u'base.mako'
_source_encoding = 'utf-8'
_exports = [u'footer', u'header', u'title', u'css', u'script']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def footer():
            return render_footer(context.locals_(__M_locals))
        def script():
            return render_script(context.locals_(__M_locals))
        self = context.get('self', UNDEFINED)
        def title():
            return render_title(context.locals_(__M_locals))
        def header():
            return render_header(context.locals_(__M_locals))
        def css():
            return render_css(context.locals_(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html>\n<!--\nIn this file all the imports of external libraries should be declared.\n-->\n<html ng-app="main">\n    <head>\n        <script src="/static/angular.js" ></script>\n        <script src="/static/jquery.min.latest.js"></script>\n        <script src="/static/bootstrap/js/bootstrap.min.js"></script>\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'script'):
            context['self'].script(**pageargs)
        

        # SOURCE LINE 10
        __M_writer(u'\n        <link href="/static/bootstrap/css/bootstrap.min.css" rel="stylesheet" media="screen">\n        <link rel="stylesheet" type="text/css" href="/static/basic.css">\n        <link rel="stylesheet" type="text/css" href="/static/toaster.css">\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'css'):
            context['self'].css(**pageargs)
        

        # SOURCE LINE 14
        __M_writer(u'\n        <title> ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        # SOURCE LINE 15
        __M_writer(u'</title>\n    </head>\n    <body>\n\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        # SOURCE LINE 30
        __M_writer(u'\n\n                        ')
        # SOURCE LINE 32
        __M_writer(unicode(self.body()))
        __M_writer(u'\n\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        # SOURCE LINE 40
        __M_writer(u'\n\n\n    </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        # SOURCE LINE 34
        __M_writer(u'\n                    </div>\n                </div>\n            </div>\n\n            <script src="/static/toaster.js"></script>\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        # SOURCE LINE 19
        __M_writer(u'\n            <toaster-container toaster-options="{\'time-out\': 6000}"></toaster-container>\n\n            <div ng-controller="IndexCtrl">\n                <div class="container">\n\n                    <div class="headline">\n                        Title\n                    </div>\n\n                    <div id="formContainer" class="jumbotron">\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_css(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def css():
            return render_css(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_script(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def script():
            return render_script(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


