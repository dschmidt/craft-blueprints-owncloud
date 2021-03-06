import info
import os

class subinfo(info.infoclass):
    def setTargets(self):
        for ver in ["master"]:
            self.svnTargets[ver] = f" https://github.com/owncloud/client|{ver}|"

        self.defaultTarget = 'master'
        self.description = "ownCloud Desktop Client"
        self.webpage = "https://owncloud.org"

    def setDependencies(self):
        self.buildDependencies["dev-util/cmake"] = "default"
        self.buildDependencies["frameworks/extra-cmake-modules"] = "default"
        self.runtimeDependencies["libs/qt5/qtbase"] = "default"
        self.runtimeDependencies["libs/qt5/qtsvg"] = "default"
        self.runtimeDependencies["libs/qt5/qtxmlpatterns"] = "default"
        self.runtimeDependencies["libs/qt5/qtwebkit"] = "default"
        self.runtimeDependencies["qt-libs/qtkeychain"] = "default"


from Package.CMakePackageBase import *

class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
        self.subinfo.options.configure.args = "-DUNIT_TESTING=1 -DWITH_TESTING=1"
