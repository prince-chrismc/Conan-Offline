from conans import python_requires

p = python_requires("jwt-cpp/0.3.1")
class Package(p.jwt_cpp):
    pass
