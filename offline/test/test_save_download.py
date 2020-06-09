from offline.save.download import download_sources
from conans.test.utils.test_files import temp_folder
from conans.util.files import save_files, load
from conans.paths import DATA_YML
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
import os


data = """sources:
  "0.2.0":
    url: "http://127.0.0.1:8000/hello.txt"
    sha256: 945ac39f14273be742c8a060af100182e38920f641e5d8fa16699e74a09e9850
"""

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('127.0.0.1', 8000)
    httpd = server_class(server_address, handler_class)

    def run_server(httpd):
      httpd.serve_forever()

    x = threading.Thread(target=run_server, args=(httpd,))
    x.start()

    return httpd, x

class FileServer():
    def __init__(self):
      self.server, self.thread = run()

    def __del__(self):
      self.server.shutdown()
      self.thread.join()

def test_save_sources():
   tmp_dir = temp_folder()
   save_files(".", {DATA_YML: data, "hello.txt": "hello world!"})
   FileServer()

   download_sources(".", "0.2.0")

   content = load(os.path.join(".", "hello.txt"))
   assert(content == "hello world!")

