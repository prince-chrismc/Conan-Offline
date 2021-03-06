from offline.edit.conandata import edit_conandata
from conans.test.utils.test_files import temp_folder
from conans.util.files import save_files
from conans.paths import DATA_YML
from os.path import join
import yaml

data = """sources:
  "1.6.1":
    url: "https://downloads.apache.org/apr/apr-util-1.6.1.tar.gz"
    sha256: "b65e40713da57d004123b6319828be7f1273fbc6490e145874ee1177e112c459"
patches:
  "1.6.1":
    - base_path: "source_subfolder"
      patch_file: "patches/0001-cmake-build-only-shared-static.patch"
    - base_path: "source_subfolder"
      patch_file: "patches/0002-apu-config-prefix-env.patch"
    - base_path: "source_subfolder"
      patch_file: "patches/0003-disable-check-APR_LIBRARIES.patch"
"""

def test_edit_conandata():
   tmp_dir = temp_folder()
   save_files(".", {DATA_YML: data})
   new_data = edit_conandata(".", "1.6.1", "ftp://my.server.com:8443")
   raw = yaml.dump(new_data)
   assert("url: ftp://my.server.com:8443/apr/apr-util-1.6.1.tar.gz" in raw)

def test_edit_conandata_with_sub_path():
   save_files(".", {DATA_YML: data})
   new_data = edit_conandata(".", "1.6.1", "ftp://my.server.com:8443/repository/abc")
   raw = yaml.dump(new_data)
   assert("url: ftp://my.server.com:8443/repository/abc/apr/apr-util-1.6.1.tar.gz" in raw)
