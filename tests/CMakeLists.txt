cmake_minimum_required(VERSION 3.15)
project(ConanCudaLibTest CXX)

find_package(GTest REQUIRED CONFIG)

add_executable(conancudalib_test conancudalib_test.cpp)
target_link_libraries(conancudalib_test conancudalib::conancudalib GTest::gtest GTest::gtest_main)