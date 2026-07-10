cmake_minimum_required(VERSION 3.20)

project(lingmo-workspace VERSION 1.0.0 DESCRIPTION "Lingmo Workspace" LANGUAGES CXX)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Qt6 COMPONENTS Core DBus Quick REQUIRED)

find_package(KF6KIO)
find_package(KF6Solid)
find_package(KF6WindowSystem)
find_package(KF6Config)

add_executable(lingmo-workspace
  main.cpp
  desktop.cpp

  desktop/desktopview.cpp
  desktop/dockdbusinterface.cpp
  desktop/desktopsettings.cpp
  thumbnailer/thumbnailprovider.cpp
  thumbnailer/thumbnailcache.cpp
  qml.qrc

  ${DBUS_SOURCES}
)

target_link_libraries(lingmo-workspace
  PRIVATE
  Qt6::Core
  Qt6::DBus
  Qt6::Quick

  KF6::KIOCore
  KF6::KIOFileWidgets
  KF6::KIOWidgets
  KF6::Solid
  KF6::WindowSystem
  KF6::ConfigCore
)

file(GLOB TS_FILES translations/*.ts)
foreach(filepath ${TS_FILES})
    string(REPLACE "${CMAKE_CURRENT_SOURCE_DIR}/" "" filename ${filepath})
    list(APPEND ts_files_replaced ${filename})
endforeach()
qt_create_translation(QM_FILES ${CMAKE_CURRENT_SOURCE_DIR} ${ts_files_replaced})

add_custom_target(translations ALL DEPENDS ${QM_FILES} SOURCES ${ts_files_replaced})

install(TARGETS lingmo-workspace RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR})
install(FILES ${QM_FILES} DESTINATION /usr/share/lingmo-workspace/translations)
