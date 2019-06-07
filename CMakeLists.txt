cmake_minimum_required(VERSION 3.5 FATAL_ERROR)
project("libcyusb")
include(GNUInstallDirs)

set(LIBCYUSB_VERSION_MAJOR 1)
set(LIBCYUSB_VERSION_MINOR 0)
set(LIBCYUSB_VERSION_PATCH 5)
set(LIBCYUSB_VERSION ${LIBCYUSB_VERSION_MAJOR}.${LIBCYUSB_VERSION_MINOR}.${LIBCYUSB_VERSION_PATCH} )

find_package(PkgConfig REQUIRED)
pkg_check_modules(libusb REQUIRED IMPORTED_TARGET libusb-1.0)
add_library(cyusb SHARED "lib/libcyusb.cpp")
set_target_properties(cyusb PROPERTIES PUBLIC_HEADER "include/cyusb.h")
target_link_libraries(cyusb PkgConfig::libusb)

set_target_properties(cyusb PROPERTIES VERSION ${LIBCYUSB_VERSION}
                                       SOVERSION ${LIBCYUSB_VERSION_MAJOR})

install(TARGETS cyusb
        EXPORT cyusbTargets
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
        ARCHIVE DESTINATION ${CMAKE_INSTALL_BINDIR}
        PUBLIC_HEADER DESTINATION  ${CMAKE_INSTALL_INCLUDEDIR})

install(FILES configs/cyusb.conf
        DESTINATION ${CMAKE_INSTALL_FULL_SYSCONFDIR})
install(FILES configs/88-cyusb.rules
        DESTINATION "${CMAKE_INSTALL_FULL_SYSCONFDIR}/udev/rules.d")

include(CMakePackageConfigHelpers)

write_basic_package_version_file("${CMAKE_CURRENT_BINARY_DIR}/cyusbConfigVersion.cmake"
    VERSION ${LIBCYUSB_VERSION}
    COMPATIBILITY AnyNewerVersion
)

configure_file(cyusbConfig.cmake "${CMAKE_CURRENT_BINARY_DIR}/cyusbConfig.cmake" COPYONLY)

set(ConfigPackageLocation "${CMAKE_INSTALL_LIBDIR}/cmake/cyusb")
install(EXPORT cyusbTargets DESTINATION "${ConfigPackageLocation}")

install(FILES "${CMAKE_CURRENT_BINARY_DIR}/cyusbConfig.cmake"
               "${CMAKE_CURRENT_BINARY_DIR}/cyusbConfigVersion.cmake"
        DESTINATION "${ConfigPackageLocation}")

set(CPACK_GENERATOR "DEB")

set(CPACK_PACKAGE_DESCRIPTION "(Unofficial) Library for cyusb")
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "(Unofficial) Library for cyusb")
set(CPACK_PACKAGE_VENDOR "hmaarrfk")
set(CPACK_PACKAGE_CONTACT "mark.harfouche@gmail.com")
set(CPACK_PACKAGE_HOMEPAGE_URL "https://github.com/hmaarrfk/libcyusb")
set(CPACK_PACKAGE_VERSION_MAJOR ${LIBCYUSB_VERSION_MAJOR})
set(CPACK_PACKAGE_VERSION_MINOR ${LIBCYUSB_VERSION_MINOR})
set(CPACK_PACKAGE_VERSION_PATCH ${LIBCYUSB_VERSION_PATCH})

set(CPACK_PACKAGE_FILE_NAME "${PROJECT_NAME}_${LIBCYUSB_VERSION_MAJOR}.${LIBCYUSB_VERSION_MINOR}.${LIBCYUSB_VERSION_PATCH}")
set(CPACK_SOURCE_PACKAGE_FILE_NAME "${PROJECT_NAME}_${LIBCYUSB_VERSION_MAJOR}.${LIBCYUSB_VERSION_MINOR}.${LIBCYUSB_VERSION_PATCH}")

set(CPACK_DEBIAN_PACKAGE_DEPENDS "libusb-1.0-0")

include(CPack)
