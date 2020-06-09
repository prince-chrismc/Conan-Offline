from conans.client.loader import ConanFileLoader
from conans.util.files import save_files
import requests


def download_sources(conanfile_path, version):
    conan_data = ConanFileLoader._load_data(conanfile_path)
    url = conan_data["sources"][version]["url"]
    filename = url.split("/")[-1]
    r = requests.get(url)
    save_files(".", {filename: r.text})
