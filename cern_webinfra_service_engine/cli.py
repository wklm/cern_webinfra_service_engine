from .activemq import create_queue
from .message_processor import MessageProcessor
from .iresource import IResource
from utils import import_string
import os




class Endpoint(IResource):

    def get(self, **kwargs):
        print('get', parameters)

    def post(self, parameters):
        pass
        # res = request.post('hostel.cern.ch/rooms', data=parameters['data'])
        # return res.json()
        # print('post', parameters)

    def delete(self, parameters):
        print('delete', parameters)



class Resources(MessageProcessor):

    def __init__(self, conn):
        super(Resources, self).__init__(conn)

        self.add_resource(Endpoint, [
            'namespace/some_endpoint/<endpoint_id>',
            'insrtance/srula/<userwdwqdid>'
        ])


print('starting the service queue...')
create_queue(Resources).connect()
