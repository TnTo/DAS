from conans import ConanFile
import os


class PkgTest(ConanFile):
    settings = 'os', 'compiler', 'build_type', 'arch'
    requires = ['Dyno/0.0.1', 'catch2/3.1.0']
    generators = 'scons'

    def build(self):
        debug_opt = '--debug-build' if self.settings.build_type == 'Debug' else ''
        self.run('scons -C {} {}'.format(self.source_folder, debug_opt))

    def test(self):
        self.run(os.path.join('.', 'test'))
