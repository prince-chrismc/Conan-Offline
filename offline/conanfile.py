from conans import python_requires

p = python_requires("zlib/1.2.11@conan/stable")
class Package(p.zlib):
    pass
