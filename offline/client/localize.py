import argparse

from offline.edit.conandata import edit_conandata
from conans.util.files import save_files
from conans.paths import DATA_YML

def localize(args):
   """coverts a conan recipe which uses a 'conandata.yml' (typically from CCI)
   to leveage a local server (like artifactory)
   """
   parser = argparse.ArgumentParser(
      description=localize.__doc__, prog="offline localize")
   parser.add_argument("--scheme", default="https",
                     help='Configure the protocol to use. e.g.: "http"')
   parser.add_argument(
      "host", help='The new server which holds the zipped sources.'
      'this can be the hostname, FQDN, or IP address.'
      'Optionally the port can be indicated.')
   parser.add_argument(
      'target', help='Path to the package folder in the user workspace')
   parser.add_argument('version', help='Version to convert. e.g.: "v1.3.0"')

   args = parser.parse_args(*args)

   data = edit_conandata(args.target, args.version, args.scheme, args.host)
   save_files(args.target, {DATA_YML: data})
