def application(environ, start_response):
    body = b"Hello, World!"
    status = "200 OK"
    headers = [("Content-Type", "text/plain"), ("Content-Length", str(len(body)))]
    start_response(status, headers)
    return [body]

if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    server = make_server("localhost", 8000, application)
    server.serve_forever()