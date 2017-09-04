class IResource:
    def post(self, parameters, message):
        raise NotImplementedError(
            "The post method wasn\'t implemented in a resource class"
        )

    def put(self, parameters, message):
        raise NotImplementedError(
            "The put method wasn\'t implemented in a resource class"
        )

    def delete(self, parameters, message):
        raise NotImplementedError(
            "The delete method wasn\'t implemented in a resource class"
        )
