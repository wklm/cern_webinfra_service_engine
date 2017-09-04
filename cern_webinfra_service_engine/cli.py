import operator

from cern_webinfra_service_engine.activemq import create_queue
from cern_webinfra_service_engine.iresource import IResource
from cern_webinfra_service_engine.message_processor import MessageProcessor


class Hello(IResource):
    def post(self, parameters, message):
        print(
            'Hello from sample webinfra service :)\n',
            'Your message: \n', message
        )


class Calculator(IResource):
    def post(self, parameters, message):
        operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            'power': operator.pow,
        }
        operation = (operations[parameters['operand']])
        number1, number2 = \
            int(parameters['number1']), \
            int(parameters['number2'])
        print(operation(number1, number2))

    def put(self, parameters, message):
        print('put', parameters, message)

    def delete(self, parameters, message):
        print('delete', parameters)


class Resources(MessageProcessor):
    def __init__(self, conn):
        super(Resources, self).__init__(conn)

        self.add_resource(Hello, [
            'hello'
        ])

        self.add_resource(Calculator, [
            'calculator/<number1>/<operand>/<number2>'
        ])


create_queue(Resources).connect()
