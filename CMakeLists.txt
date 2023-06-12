cmake_minimum_required(VERSION 3.24)

message(STATUS "Building with CMake version: ${CMAKE_VERSION}")

set(CMAKE_CUDA_ARCHITECTURES 52 61 CACHE STRING "Define the Cuda Architectures manualy (ex: \"52;61\")")

project(conancudalib
    VERSION 1.0.0
    LANGUAGES CUDA CXX
)

# ---------------------------------------------
# Options
#
option(WITH_TESTS "Build library tests" OFF)

# ---------------------------------------------
# Find packages
#
find_package(CUDAToolkit REQUIRED)

# --------------------------------------------
# Library - Compilation with CUDA
#
add_library(${PROJECT_NAME} STATIC "")
add_library(${PROJECT_NAME}::${PROJECT_NAME} ALIAS ${PROJECT_NAME})
set_target_properties(${PROJECT_NAME} PROPERTIES CUDA_STANDARD 17)
set_target_properties(${PROJECT_NAME} PROPERTIES DEBUG_POSTFIX "d")


target_link_libraries(${PROJECT_NAME}
    PUBLIC
        CUDA::cudart_static
)

target_include_directories(${PROJECT_NAME}
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/include
    PUBLIC
        ${CMAKE_CUDA_TOOLKIT_INCLUDE_DIRECTORIES}
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>
)

target_compile_options(${PROJECT_NAME}
    PRIVATE
        "$<$<COMPILE_LANGUAGE:CUDA>:-m64>"
)

add_subdirectory(include)
add_subdirectory(src)

# ----------------------------------------------------
# Unit Testing Section
#
if(GASREA_BUILD_TESTS)
    add_subdirectory(tests)
endif()

# ----------------------------------------------------
# Installation Section
#
# definitions of CMAKE_INSTALL_LIBDIR, CMAKE_INSTALL_INCLUDEDIR and others
include(GNUInstallDirs)
# paths for binaries and headers
install(TARGETS ${PROJECT_NAME}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR} # bin
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR} # lib
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR} # lib
    INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR} # include
    PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/${PROJECT_NAME} # include/conancudalib
)
