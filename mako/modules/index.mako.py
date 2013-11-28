# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1385645250.308221
_enable_loop = True
_template_filename = 'mako/htdocs/index.mako'
_template_uri = 'index.mako'
_source_encoding = 'utf-8'
_exports = []


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
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n<!--\nThis is the content part of the Mako template. This project uses two frameworks:\n\nBootstrap which supplies graphical components like buttons and icon. It also supports responsive design.\nMore info at http://getbootstrap.com/\n\nAngularJs which generates html code based on javascript objects. Read more at http://docs.angularjs.org/api/\n\nThere is also a javascript based notification library Toaster which uses AngularJS.\nToaster is used for displaying notifications in a nice way.\n-->\n\n\n<toaster-container toaster-options="{\'time-out\': 6000}"></toaster-container>\n\n<div ng-controller="IndexCtrl">\n    <div class="container">\n\n        <div class="headline">\n            Title\n        </div>\n\n        <div id="formContainer" class="jumbotron">\n\n\n            <div>Test text that is in the file index.mako</div>\n\n            <br>\n\n            <!-- The Bootstrap framework contains over 200 different icons which could be used -->\n            <span class="glyphicon glyphicon-info-sign" rel="tooltip" title="{{data.descr}}" id="infoIcon"></span>\n\n            <br>\n\n            <!-- Two Bootstrap button which have a AngularJS click trigger -->\n            <button class="btn btn-primary btn-sm" ng-click="addElement(\'Button element\');">Add item to list</button>\n            <button class="btn btn-primary btn-sm" ng-click="getElementsFromServer();">Get Elements From Server</button>\n\n            <!-- A loop which creates new div tags for every element in the variable $scope.list (defined in test.js).\n                 Only elements which doesn\'t have a attribute called visible not equal false will be presented in the list -->\n            <div ng-repeat="element in list" ng-show="element.visible != false">{{element.id}}</div>\n        </div>\n    </div>\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


