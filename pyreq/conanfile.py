from conans import ConanFile

class PyReq(ConanFile):
    name = "pyreq"
    version = "0.1"

    def source(self):
        self.output.info("My cool source!")
    def build(self):
        self.output.info("My cool build!")
    def package(self):
        self.output.info("My cool package!")
    def package_info(self):
        self.output.info("My cool package_info!")