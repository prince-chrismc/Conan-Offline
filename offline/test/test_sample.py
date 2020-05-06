from conans.test.utils.tools import TestClient

def func(x):
    return x + 1

def test_requires():
    conanfile = """from conans import ConanFile
class MyConanfileBase(ConanFile):
    def source(self):
        self.output.info("My cool source!")
    def build(self):
        self.output.info("My cool build!")
    def package(self):
        self.output.info("My cool package!")
    def package_info(self):
        self.output.info("My cool package_info!")
"""
    client = TestClient()
    client.save({"conanfile.py": conanfile})
    client.run("export . MyConanfileBase/1.1@lasote/testing")
    assert func(3) == 4
