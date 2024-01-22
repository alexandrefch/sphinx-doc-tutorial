cmake_minimum_required(VERSION 3.0.0)
project(my_project VERSION 0.1.0 LANGUAGES C CXX)

add_compile_options(-std=c++17)

file(GLOB_RECURSE SRC_FILES
    ${PROJECT_SOURCE_DIR}/src/*.cpp
    ${PROJECT_SOURCE_DIR}/include/*.h
)

include_directories(${PROJECT_SOURCE_DIR}/include())
add_executable(my_project ${SRC_FILES})