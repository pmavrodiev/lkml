cmake_minimum_required(VERSION 2.6)
project(scrapy_tutorial)

add_executable(scrapy_tutorial main.cpp)

install(TARGETS scrapy_tutorial RUNTIME DESTINATION bin)
