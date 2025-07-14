cmake_minimum_required(VERSION 3.12)
project(trading_system)

# C++ Standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find required packages
find_package(pybind11 REQUIRED)
find_package(GTest REQUIRED)
find_package(Threads REQUIRED)

# Include directories
include_directories(include)

# Source files für die Hauptbibliothek
set(SOURCES
    src/account.cpp
    src/good.cpp
    src/market.cpp
    src/price_generator.cpp
    src/user.cpp
)

# Hauptbibliothek erstellen - WICHTIG: Mit -fPIC für shared libraries
add_library(trading_lib STATIC ${SOURCES})
set_target_properties(trading_lib PROPERTIES POSITION_INDEPENDENT_CODE ON)

# Python-Bindings
pybind11_add_module(unolib extra/bindings.cpp)
target_link_libraries(unolib PRIVATE trading_lib)

# Compiler-spezifische Eigenschaften für Python-Modul
target_compile_definitions(unolib PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})

# Unit Tests
add_executable(run_tests tests/tests.cpp)
target_link_libraries(run_tests 
    trading_lib 
    GTest::gtest 
    GTest::gtest_main
    Threads::Threads
)

# Test-Target hinzufügen
enable_testing()
add_test(NAME unit_tests COMMAND run_tests)

