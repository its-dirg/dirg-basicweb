# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1385732813.748911
_enable_loop = True
_template_filename = 'mako/htdocs/index.mako'
_template_uri = 'index.mako'
_source_encoding = 'utf-8'
_exports = [u'body', u'footer', u'title', u'header', u'script', u'css']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def body():
            return render_body(context.locals_(__M_locals))
        parent = context.get('parent', UNDEFINED)
        def script():
            return render_script(context.locals_(__M_locals))
        def title():
            return render_title(context.locals_(__M_locals))
        def header():
            return render_header(context.locals_(__M_locals))
        def footer():
            return render_footer(context.locals_(__M_locals))
        def css():
            return render_css(context.locals_(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'<!--\nYou must install dirg-util to be able to use dirg-base.mako\n-->\n')
        # SOURCE LINE 5
        __M_writer(u'\n<!--\nThis is the content part of the Mako template. This project uses two frameworks:\n\nBootstrap which supplies graphical components like buttons and icon. It also supports responsive design.\nMore info at http://getbootstrap.com/\n\nAngularJs which generates html code based on javascript objects. Read more at http://docs.angularjs.org/api/\n\nThere is also a javascript based notification library Toaster which uses AngularJS.\nToaster is used for displaying notifications in a nice way.\n\nPlease view static/test.js for more example of angular and toaster.\n-->\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'script'):
            context['self'].script(**pageargs)
        

        # SOURCE LINE 23
        __M_writer(u'\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'css'):
            context['self'].css(**pageargs)
        

        # SOURCE LINE 29
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        # SOURCE LINE 34
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        # SOURCE LINE 38
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body'):
            context['self'].body(**pageargs)
        

        # SOURCE LINE 58
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body():
            return render_body(context)
        __M_writer = context.writer()
        # SOURCE LINE 40
        __M_writer(u'\n    <div>Test text that is in the file index.mako</div>\n\n    <br>\n\n    <!-- The Bootstrap framework contains over 200 different icons which could be used -->\n    <span class="glyphicon glyphicon-info-sign" rel="tooltip" title="{{data.descr}}" id="infoIcon"></span>\n\n    <br>\n\n    <!-- Two Bootstrap button which have a AngularJS click trigger -->\n    <button class="btn btn-primary btn-sm" ng-click="addElement(\'Button element\');">Add item to list</button>\n    <button class="btn btn-primary btn-sm" ng-click="getElementsFromServer();">Get Elements From Server</button>\n\n    <!-- A loop which creates new div tags for every element in the variable $scope.list (defined in test.js).\n         Only elements which doesn\'t have a attribute called visible not equal false will be presented in the list -->\n    <div ng-repeat="element in list" ng-show="element.visible != false">{{element.id}}</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        # SOURCE LINE 60
        __M_writer(u'\n    <script src="/static/test.js"></script>\n    ')
        # SOURCE LINE 62
        __M_writer(unicode(parent.footer()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        def title():
            return render_title(context)
        __M_writer = context.writer()
        # SOURCE LINE 31
        __M_writer(u'\n    My test application\n    ')
        # SOURCE LINE 33
        __M_writer(unicode(parent.title()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 36
        __M_writer(u'\n    ')
        # SOURCE LINE 37
        __M_writer(unicode(parent.header()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_script(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        def script():
            return render_script(context)
        __M_writer = context.writer()
        # SOURCE LINE 20
        __M_writer(u'\n    <!-- Add more script imports here! -->\n    ')
        # SOURCE LINE 22
        __M_writer(unicode(parent.script()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_css(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        def css():
            return render_css(context)
        __M_writer = context.writer()
        # SOURCE LINE 26
        __M_writer(u'\n    <!-- Add more css imports here! -->\n    ')
        # SOURCE LINE 28
        __M_writer(unicode(parent.script()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


