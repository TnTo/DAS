cmake_minimum_required(VERSION 3.20)
project(DAS LANGUAGES CXX)

set(CMAKE_VERBOSE_MAKEFILE OFF)

find_package(Dyno REQUIRED)

file(GLOB_RECURSE cxx_sources CONFIGURE_DEPENDS "src/DAS/*.cpp")

add_executable(DAS src/DAS.cpp ${cxx_sources})
target_link_libraries(DAS Dyno::Dyno)