from conans import python_requires, tools

base = python_requires("jwt-cpp/0.3.1")
class PkgTest(base.JwtCppConan):
   exports_sources = "source_subfolder/**"

   def source(self):
      extracted_dir = self.name + "-" + self.version
      self.copy(extracted_dir, self._source_subfolder)
      for patch in self.conan_data["patches"][self.version]:
         tools.patch(**patch)
