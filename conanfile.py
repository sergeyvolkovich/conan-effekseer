from   conans       import ConanFile, CMake, tools
from   distutils.dir_util import copy_tree
import os

class EffekseerConan(ConanFile):
    name            = "effekseer"
    version         = "170e"
    description     = "Conan package for Effekseer runtime."
    url             = "https://github.com/effekseer/Effekseer"
    license         = "MIT"
    settings        = "arch", "os", "compiler", "build_type"
    generators      = "cmake"
    options         = {
            "shared": [True, False]
            }
    default_options = {
            "shared": False
            }

    def source(self):
        git = tools.Git(folder="source_subfolder")
        git.clone("https://github.com/effekseer/Effekseer", self.version)

    def build(self):
        cmake          = CMake(self)
        options = {
            "BUILD_SHARED_LIBS": self.options.shared,
            "BUILD_VIEWER": False,
            "BUILD_TEST": False,
            "BUILD_EXAMPLES": False,
            "BUILD_DX9": False,
            "BUILD_DX11": False,
            "BUILD_DX12": False,
            "BUILD_VULKAN": False,
            "BUILD_METAL" : False,
            "BUILD_GL": False,
            "USE_OPENGLES2": False,
            "USE_OPENGLES3": False,
            "USE_OPENGL3": False,
            "USE_OPENAL": False,
            "USE_XAUDIO2": False,
            "USE_DSOUND": False,
            "USE_OSM": False,
            "USE_INTERNAL_LOADER": False,
            }

        if self.settings.os == "Windows":
            options['USE_MSVC_RUNTIME_LIBRARY_DLL'] = "MD" in self.settings.compiler.runtime

        cmake.configure(source_folder="source_subfolder", build_folder="build_subfolder", defs=options)
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("*.h"  , dst="include", src="include/", keep_path=False)
        self.copy("*.hpp", dst="include", src="include/", keep_path=False)
        self.copy("*.inl", dst="include", src="include/", keep_path=False)
        self.copy("*.a", dst="lib", src="lib", keep_path=False)
        self.copy("*.lib", dst="lib", src="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["Effekseer"]
        self.cpp_info.includedirs = ["include/Effekseer"]
        self.cpp_info.builddirs = ["lib"]
