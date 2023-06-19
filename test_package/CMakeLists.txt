cmake_minimum_required(VERSION 3.24)
project(PackageTest CUDA CXX)

find_package(CUDAToolkit REQUIRED)
find_package(conancudalib CONFIG REQUIRED)

add_executable(example src/example.cpp)

target_link_directories(example PRIVATE ${CUDAToolkit_LIBRARY_DIR})
target_link_libraries(example CUDA::cudart_static conancudalib::conancudalib)
