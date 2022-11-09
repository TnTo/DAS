from conans import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout


class Pkg(ConanFile):

    name = 'DAS'
    version = '0.0.1'
    license = 'MIT'
    author = "Michele Ciruzzi tnto@hotmail.it"
    url = 'https://www.github.com/TnTo/DAS'
    settings = 'os', 'compiler', 'build_type', 'arch'
    description = 'Dreaming of Artificial Societies'
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    exports_sources = 'src/*'

    requires = ['Dyno/0.0.1']

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

        if self.settings.compiler == "Visual Studio":
            self.settings.compiler.cppstd = '20'
        else:
            self.settings.compiler.cppstd = 'gnu20'

        self.settings.compiler.libcxx = "libstdc++11"

    def layout(self):
        cmake_layout(self, build_folder='build')

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("DAS", src=".", dst="bin", keep_path=False)
