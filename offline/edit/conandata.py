from conans.client.loader import ConanFileLoader
import urllib.parse


def edit_conandata(conanfile_path, version, new_base_url):
    conan_data = ConanFileLoader._load_data(conanfile_path)
    url = conan_data["sources"][version]["url"]
    olds_parts = urllib.parse.urlparse(url)
    new_parts = urllib.parse.urlparse(new_base_url)
    new_parts = new_parts._replace(path=new_parts.path + olds_parts.path)
    new_url = new_parts.geturl()
    conan_data["sources"][version]["url"] = new_url
    return conan_data