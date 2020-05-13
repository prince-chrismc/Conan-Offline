
from conans.client.loader import ConanFileLoader
import urllib.parse


def edit_conandata(conanfile_path, version, scheme, netloc):
    conan_data = ConanFileLoader._load_data(conanfile_path)
    url = conan_data["sources"][version]["url"]
    parts = urllib.parse.urlparse(url)
    parts = parts._replace(scheme=scheme)
    parts = parts._replace(netloc=netloc)
    new_url = parts.geturl()
    conan_data["sources"][version]["url"] = new_url
    return conan_data