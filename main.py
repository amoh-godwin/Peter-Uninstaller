# -*- coding: utf-8 -*-
import sys
import os
from PyQt5.QtCore import QCoreApplication, QSettings, QResource
from PyQt5.QtGui import QGuiApplication, QIcon
from PyQt5.QtQml import QQmlApplicationEngine

from connector import Connector 

QResource.registerResource('uninstall.rcc')
QCoreApplication.setOrganizationName("Deuteronomy Works")
QCoreApplication.setApplicationName("Peter Uninstaller")
settings = QSettings()

os.environ["QT_QUICK_CONTROLS_STYLE"] = "Universal"
app = QGuiApplication(sys.argv)
app.setWindowIcon(QIcon(":UI/images/Peter.png"))

connect = Connector()

engine = QQmlApplicationEngine()
engine.rootContext().setContextProperty('Connector', connect)
engine.load('qrc:///UI/qml/main.qml')
engine.quit.connect(app.quit)

sys.exit(app.exec_())
