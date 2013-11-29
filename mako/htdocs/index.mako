## index.html
<!--
You must install dirg-util to be able to use dirg-base.mako
-->
<%inherit file="base.mako"/>
<!--
This is the content part of the Mako template. This project uses two frameworks:

Bootstrap which supplies graphical components like buttons and icon. It also supports responsive design.
More info at http://getbootstrap.com/

AngularJs which generates html code based on javascript objects. Read more at http://docs.angularjs.org/api/

There is also a javascript based notification library Toaster which uses AngularJS.
Toaster is used for displaying notifications in a nice way.

Please view static/test.js for more example of angular and toaster.
-->

<%block name="script">
    <!-- Add more script imports here! -->
    ${parent.script()}
</%block>


<%block name="css">
    <!-- Add more css imports here! -->
    ${parent.script()}
</%block>

<%block name="title">
    My test application
    ${parent.title()}
</%block>

<%block name="header">
    ${parent.header()}
</%block>

<%block name="body">
    <div>Test text that is in the file index.mako</div>

    <br>

    <!-- The Bootstrap framework contains over 200 different icons which could be used -->
    <span class="glyphicon glyphicon-info-sign" rel="tooltip" title="{{data.descr}}" id="infoIcon"></span>

    <br>

    <!-- Two Bootstrap button which have a AngularJS click trigger -->
    <button class="btn btn-primary btn-sm" ng-click="addElement('Button element');">Add item to list</button>
    <button class="btn btn-primary btn-sm" ng-click="getElementsFromServer();">Get Elements From Server</button>

    <!-- A loop which creates new div tags for every element in the variable $scope.list (defined in test.js).
         Only elements which doesn't have a attribute called visible not equal false will be presented in the list -->
    <div ng-repeat="element in list" ng-show="element.visible != false">{{element.id}}</div>

</%block>

<%block name="footer">
    <script src="/static/test.js"></script>
    ${parent.footer()}
</%block>