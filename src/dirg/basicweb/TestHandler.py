# -*- coding: utf-8 -*-
import json
import subprocess
from dirg_util.http_util import Response, ServiceError

__author__ = 'haho0032'


class Test:
    IDP_TESTDRV = '/usr/local/bin/idp_testdrv.py'
    CONFIG_FILE_PATH = 'saml2test/configFiles/'

    def __init__(self, environ, start_response, session, logger, lookup, config, parameters):
        """
        Constructor for the class.
        :param environ:        WSGI enviroment
        :param start_response: WSGI start_respose
        :param session:        Beaker session
        :param logger:         Class to perform logging.
        """
        self.environ = environ
        self.start_response = start_response
        self.session = session
        self.logger = logger
        self.lookup = lookup
        self.config = config
        self.parameters = parameters
        self.urls = {
            "": "index.mako",
            "list": None
        }

    def verify(self, path):
        for url, file_ in self.urls.iteritems():
            if path == url:
                return True

    def handle(self, path):
        if path == "":
            return self.handle_index(self.urls[path])
        elif path == "list":
            return self.handle_list()

    def handle_index(self, file_):
        resp = Response(mako_template=file_,
                        template_lookup=self.lookup,
                        headers=[])
        argv = {
            "a_value": "Hello world"
        }
        return resp(self.environ, self.start_response, **argv)


    def handle_list(self):
        parameter = self.parameters['parameter']

        if parameter == "testParameter":
            result = [{'id': 'server element1'}, {'id': 'server element2'}, {'id': 'server element3'}]
            my_json = json.dumps(result)

        else:
            return self.service_error("Cannot list the tests.")

        return self.return_json(my_json)

    def return_json(self, text):
        resp = Response(text, headers=[('Content-Type', "application/json")])
        return resp(self.environ, self.start_response)


    def service_error(self, message):
        message = {"ExceptionMessage": message}
        resp = ServiceError(json.dumps(message))
        return resp(self.environ, self.start_response)


    def run_script(self, command, working_directory=None):
        try:
            p = subprocess.Popen(command,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 cwd=working_directory)
            while True:
                retcode = p.poll() #returns None while subprocess is running
                if retcode is not None:
                    break
            p_out = p.stdout.read()
            p_err = p.stderr.read()
            return True, p_out, p_err
        except Exception as ex:
            self.logger.fatal("Can not run command: +" + ex.message)
            return False, None, None