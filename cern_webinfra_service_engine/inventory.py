import requests
import os
class InventoryWrapper():
    def __init__(self):

        self.api_root = os.environ['INVENTORY_ADDRESS']
        self.endpoints = \
            [endpoint for endpoint in requests.get(self.api_root).json()]

    def get_model_schema(self, endpoint):
        return requests.options(self.api_root + '/rest/namespace/instance/?format=api')
        # return requests.options(os.environ['INVENTORY_ADDRESS'] + '/' + endpoint + '/?format=api')





i = InventoryWrapper()

a = i.endpoints[1]

r = i.get_model_schema(a)

print(r.json())
