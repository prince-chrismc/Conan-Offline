from conans import ConanFile


class Pkg(ConanFile):
    name = "pkg"
    python_requires = "pyreq/0.1@user/channel"
    python_requires_extend = "pyreq.PyReq"

    def source(self):
        self.output.info("********************My cool source!")
