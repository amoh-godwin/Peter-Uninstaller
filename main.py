# -*- coding: utf-8 -*-
import sys
import os
from PyQt5.QtCore import QCoreApplication, QSettings
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine

from connector import Connector 

QCoreApplication.setOrganizationName("Deuteronomy Works")
QCoreApplication.setApplicationName("Peter Uninstaller")
settings = QSettings()

os.environ["QT_QUICK_CONTROLS_STYLE"] = "Universal"
app = QGuiApplication(sys.argv)

connect = Connector()

engine = QQmlApplicationEngine()
engine.rootContext().setContextProperty('Connector', connect)
engine.load('UI/qml/main.qml')
engine.quit.connect(app.quit)

sys.exit(app.exec_())
