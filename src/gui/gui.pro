QT += quick
QT += core
QT += widgets

CONFIG += c++11
CONFIG += qtquickcompiler
QMAKE_CXXFLAGS += /Zi
QMAKE_LFLAGS += /DEBUG

TARGET = AmelieBot
RC_ICONS = src/view/res/images/icon.ico

RC_FILE = resourceExeInfo.rc


DEFINES += QT_DEPRECATED_WARNINGS


HEADERS += \
    src/core/amelie.h \
    src/core/dllimport.inl

SOURCES += \
    src/core/amelie.cpp \
    src/core/main.cpp


RESOURCES += \
    src/view/qml.qrc

TRANSLATIONS += \
    gui_en_US.ts

DISTFILES += \
    src/view/MessageItem.qml \
    src/view/main.qml \
    src/view/gui_en_US.ts \
    src/view/settingsWindow.qml
