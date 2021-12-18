import requests


class Request:
    def __init__(self, url):
        self.url = url
        self.headers = {}
        self.json = {}
        self.data = None

    def set_json(self, name, value):
        self.json[name] = value
        return self

    def set_data(self, path):
        self.data = path
        return self
    def set_header(self, name, value):
        self.headers[name] = value
        return self


class GetRequest(Request):
    def __init__(self, url):
        super().__init__(url)

    def send(self):
        return requests.get(self.url, headers=self.headers)


class PostRequest(Request):
    def __init__(self, url):
        super().__init__(url)

    def send(self):
        return requests.post(self.url, headers=self.headers, json=self.json, data=self.data)


class PutRequest(Request):
    def __init__(self, url):
        super().__init__(url)

    def send(self):
        return requests.put(self.url, headers=self.headers, json=self.json, data=self.data)


class DeleteRequest(Request):
    def __init__(self, url):
        super().__init__(url)

    def send(self):
        return requests.delete(self.url, headers=self.headers)
