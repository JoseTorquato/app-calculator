class HTTPRequest:
    def __init__(self, body, headers, method, url) -> None:
        self.headers = headers
        self.body = body
        self.method = method
        self.url = url
