# -*- coding: utf-8 -*-
import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine

app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()

engine.rootContext().setContextProperty()

engine.load('')

engine.quit.connect(app.quit)

sys.exit(app.exec_())
