from features.storage.Request import GetRequest, PutRequest, PostRequest, DeleteRequest


class FactoryPattern:
    request_type = {'GET': GetRequest,
                    'POST': PostRequest,
                    'PUT': PutRequest,
                    'DELETE': DeleteRequest}
    def get_request(self, method: str, url: str, token, content_type, headers: dict, body: dict, path: str):
        req = self.request_type[method.upper()](url)
        req.set_header('Content-Type',content_type)
        req.set_header('Authorization', ' '.join(['bearer', token]))

        for header in headers.keys():
            req.set_header('Authorization', ' '.join(['bearer', token]))
            req.set_header(header, headers[header])

        for s in body.keys():
            req.set_json(s, body[s])

        if path != '':
            req.set_data(path)

        return req
