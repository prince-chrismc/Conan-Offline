
from conans.client.loader import ConanFileLoader
import urllib.parse


def edit_conandata(conanfile_path, version):
    conan_data = ConanFileLoader._load_data(conanfile_path)
    url = conan_data["sources"][version]["url"]
    parts = urllib.parse.urlparse(url)
    parts = parts._replace(scheme='http')
    parts = parts._replace(netloc='localserver')
    new_url = parts.geturl()
    print(new_url)
    conan_data["sources"][version]["url"] = new_url
    return conan_data