"""
This is the fake SSL server that fools Amazon Dash button to make it believe
this is its mothership. You need the cert.pem file.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl


class HTTPServer_RequestHandler(BaseHTTPRequestHandler):
    """Handler class"""

    def do_GET(self):
        """Handle GET."""

        # Send response status code
        self.send_response(200)

        # Send headers
        #self.send_header('Content-type','text/html')
        #self.end_headers()
        return


def run():
    """Run the server."""
    print('starting server...')

    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('', 443)
    httpd = HTTPServer(server_address, HTTPServer_RequestHandler)
    httpd.socket = ssl.wrap_socket(httpd.socket, certfile='cert.pem', server_side=True)
    print('running server...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
