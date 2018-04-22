cmake_minimum_required(VERSION 3.5 FATAL_ERROR)
project("cyusb")
include(GNUInstallDirs)

add_library(cyusb SHARED "lib/libcyusb.cpp")
set_target_properties(cyusb PROPERTIES PUBLIC_HEADER "include/cyusb.h")
target_link_libraries(cyusb usb-1.0)

install(TARGETS cyusb
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
        ARCHIVE DESTINATION ${CMAKE_INSTALL_BINDIR}
        PUBLIC_HEADER DESTINATION  ${CMAKE_INSTALL_INCLUDEDIR})
