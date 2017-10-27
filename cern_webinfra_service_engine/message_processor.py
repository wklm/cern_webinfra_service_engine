import json
import re
import traceback
from abc import ABCMeta

from .exceptions import MethodNotAllowed


class MessageProcessor(metaclass=ABCMeta):
    def __init__(self, conn):
        self.queue_connection = conn
        self.routes = {}

    def process(self, headers, message):
        m = json.loads(message)
        method = m['http_method']
        try:
            params, resource = self._get_route(m['path'])
            methods = {
                'POST': resource.post,
                'PUT': resource.put,
                'DELETE': resource.delete
            }
            methods[method](self, params, m)
        except KeyError:
            raise MethodNotAllowed(method)
        except TypeError:
            pass
        except Exception as e:
            raise e
            # TODO self._update_request_status(self, 'stack_trace', tb_dict)



    def add_resource(self, resource, paths):
        for path in paths:
            self.routes[
                self._get_path_pattern(path)
            ] = resource

    @staticmethod
    def _get_path_pattern(path):
        return re.compile("^{}$".format(
            re.sub(r'(<\w+>)', r'(?P\1.+)', path))
        )

    def _get_route(self, path):
        for route in self.routes.keys():
            m = route.match(path)
            if m:
                return m.groupdict(), self.routes[route]
        return

    def _acknowledge(self, message_id):  # TODO
        self._update_request_status()
        self.queue_connection.ack(
            message_id.ack()
        )

    def _update_request_status(self, field, content):
        pass
