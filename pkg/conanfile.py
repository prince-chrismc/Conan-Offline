from conans import python_requires

p = python_requires("pyreq/0.1@user/channel")
class Pkg(p.PyReq):
    def source(self):
        self.output.info("My cool source!")
