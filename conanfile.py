from conans import ConanFile, tools


class Pkg(ConanFile):

    name = 'DAS'
    version = '0.0.1'
    license = 'MIT'
    author = "Michele Ciruzzi tnto@hotmail.it"
    url = 'https://www.github.com/TnTo/DAS'
    settings = 'os', 'compiler', 'cppstd', 'build_type', 'arch'
    description = 'Dreaming of Artificial Societies'
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    exports_sources = 'src/*'
    generators = 'scons'

    requires = 'Dyno/0.0.1'

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

        self.settings.compiler.libcxx = "libstdc++11"

        if self.settings.compiler == "Visual Studio":
            self.settings.cppstd = '17'
        else:
            self.settings.cppstd = 'gnu17'

    def build(self):
        debug_opts = [
            '--debug-build'] if self.settings.build_type == 'Debug' else []
        tools.mkdir("build")
        with tools.chdir("build"):
            self.run(
                ['scons', '-C', '{}/src'.format(self.source_folder)] + debug_opts)

    def package(self):
        self.copy("DAS", src=".", dst="bin", keep_path=False)
