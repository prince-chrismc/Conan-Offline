from conans.test.utils.tools import TestClient

def test_requires():
    client = TestClient()
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
    client.save({"conanfile.py": conanfile})
    client.run("export . MyConanfileBase/1.1@lasote/testing")

    reuse = """from conans import python_requires
base = python_requires("MyConanfileBase/1.1@lasote/testing")
class PkgTest(base.MyConanfileBase):
    pass
"""

    client.save({"conanfile.py": reuse}, clean_first=True)
    client.run("create . Pkg/0.1@lasote/testing")
    assert("Pkg/0.1@lasote/testing: My cool source!" in client.out)
    assert("Pkg/0.1@lasote/testing: My cool build!" in client.out)
    assert("Pkg/0.1@lasote/testing: My cool package!" in client.out)
    assert("Pkg/0.1@lasote/testing: My cool package_info!" in client.out)

def test_override_requires():
    client = TestClient()
    conanfile = """from conans import ConanFile
class MyConanfileBase(ConanFile):
    def source(self):
        self.output.info("My base source!")
    def build(self):
        self.output.info("My base build!")
    def package(self):
        self.output.info("My base package!")
    def package_info(self):
        self.output.info("My base package_info!")
"""
    client.save({"conanfile.py": conanfile})
    client.run("export . MyConanfileBase/1.1@lasote/testing")

    reuse = """from conans import python_requires
base = python_requires("MyConanfileBase/1.1@lasote/testing")
class PkgTest(base.MyConanfileBase):
    def source(self):
        self.output.info("My pkg source!")
    def build(self):
        self.output.info("My pkg build!")
    def package(self):
        self.output.info("My pkg package!")
    def package_info(self):
        self.output.info("My pkg package_info!")
"""

    client.save({"conanfile.py": reuse}, clean_first=True)
    client.run("create . Pkg/0.1@lasote/testing")
    assert("Pkg/0.1@lasote/testing: My pkg source!" in client.out)
    assert("Pkg/0.1@lasote/testing: My pkg build!" in client.out)
    assert("Pkg/0.1@lasote/testing: My pkg package!" in client.out)
    assert("Pkg/0.1@lasote/testing: My pkg package_info!" in client.out)