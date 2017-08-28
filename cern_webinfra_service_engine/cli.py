import operator

from .activemq import create_queue
from .iresource import IResource
from .message_processor import MessageProcessor


class Calculator(IResource):
    def post(self, parameters):
        operations = {
            '+': operator.add,
            '-': operator.sub,
        }
        operation = (operations[parameters['operand']])
        n1, n2 = \
            int(parameters['number1']), \
            int(parameters['number2'])
        print(operation(n1, n2))

    def put(self, parameters):
        print('put', parameters)

    def delete(self, parameters):
        print('delete', parameters)


class Resources(MessageProcessor):
    def __init__(self, conn):
        super(Resources, self).__init__(conn)

        self.add_resource(Calculator, [
            'calculator/<number1>/<operand>/<number2>'
        ])


create_queue(Resources).connect()
