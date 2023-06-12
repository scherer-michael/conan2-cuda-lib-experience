from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.build import check_min_cppstd, check_max_cppstd


class ConanCudaLibRecipe(ConanFile):
    name = "conancudalib"
    version = "1.0"

    license = "MIT"
    topics = ("conan", "cuda")
    package_type = "library"

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "with_tests": [True, False]
    }
    default_options = {
        "shared": False,
        "fPIC": True,
        "with_tests": False
    }

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    def requirements(self):
        if self.options.with_tests:
            self.test_requires("gtest/1.13.0")

    def build_requirements(self):
        self.tool_requires("cmake/3.26.4")

    def layout(self):
        cmake_layout(self)

    def validate(self):
        check_min_cppstd(self, "17")
        check_max_cppstd(self, "17") # Because of CUDA 11.x language version limit

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        suffix = "d" if self.settings.build_type == "Debug" else ""
        self.cpp_info.libs = [f"conancudalib{suffix}"]
        self.cpp_info.set_property("cmake_target_name", f"conancudalib::conancudalib{suffix}")
