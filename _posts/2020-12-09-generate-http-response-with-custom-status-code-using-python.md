---
title: "Generate HTTP Response with custom Status Code"
date: 2020-12-09T17:07:43
categories: ["Tool", "Tuts"]
tags: ["Security"]
image: /assets/uploads/2020/12/python-http-response.jpg
---

During an assessment, I needed a web server which would serve a 204 HTTP response. Is is not so common or easy to find it, so I decided to create one for when needed, which I would be able to use it offline.  
Just save the snippet below as a python file and change the status code. When loading the page, it will serve you the status code needed.

```python
from http.server import HTTPServer, BaseHTTPRequestHandler

ADDRESS = ""
PORT = 8000

class RequestHandler(BaseHTTPRequestHandler): 
    def do_GET(self):
        # Select the HTTP Response needed, currently it's 204
        self.send_response(204)

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = (ADDRESS, PORT)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == '__main__':
    run(handler_class=RequestHandler)
```
