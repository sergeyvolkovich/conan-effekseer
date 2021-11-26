cmake_minimum_required(VERSION 2.8)
project(effekseer_test)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)

conan_basic_setup(TARGETS)

add_executable( effekseer_test main.cpp )

target_compile_features( effekseer_test PUBLIC cxx_std_17 )
target_link_libraries( effekseer_test CONAN_PKG::effekseer )
