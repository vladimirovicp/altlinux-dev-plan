cmake_minimum_required(VERSION 3.31.7)

project(start)

# Говорит о том, что Cmake следует использовать С++20
set(CMAKE_CXXSTANDARD 20)

add_executable(start
    main.cpp    
)