from conans import ConanFile

class Pkg(ConanFile):
    python_requires = "pyreq/0.1@user/channel"
    python_requires_extend = "pyreq.MyBase"