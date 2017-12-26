def connected(function):
    """
    Decorator that checks the api status
    before doing any request
    """
    def check_connection(self, *args, **kwargs):
        if self.api is None:
            self.connect()
        function(self, *args, **kwargs)
    return check_connection
