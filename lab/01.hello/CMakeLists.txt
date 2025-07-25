cmake_minimum_required(VERSION 3.31.7)

project(Hello)

# Говорит о том, что Cmake следует использовать С++20
set(CMAKE_CXXSTANDARD 20)

add_executable(Hello
    main.cpp    
)