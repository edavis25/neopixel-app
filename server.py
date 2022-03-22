import board
import json
import neopixel
import os
import sys
import time
from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

hostName = "0.0.0.0"
serverPort = 3001

# initialize NeoPixel board
num_pixels = 90 # 3 strips x 30 lights/strip
pixels = neopixel.NeoPixel(board.D18, num_pixels, brightness=1)

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # Route serve the main HTML page
        if self.path == '/':
            with open(os.path.join(sys.path[0], "index.html"), "r") as fh:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(fh.read().encode())

        # Route serving the app.js scripts
        if self.path == '/app.js':
            self.send_response(200)
            self.send_header("Content-type", "application/javascript")
            self.end_headers()
            with open(os.path.join(sys.path[0], "app.js"), "r") as fh:
                self.wfile.write(fh.read().encode())

        # Route to set color of NeoPixel strips
        if self.path.split('?')[0] == '/set-color':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            query_components = parse_qs(urlparse(self.path).query)
            color = eval(query_components['color'][0])
            pixels.fill(color)

            self.wfile.write(json.dumps({'success': True }).encode())


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
