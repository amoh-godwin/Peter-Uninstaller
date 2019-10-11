# -*- coding: utf-8 -*-
import threading
from time import sleep
import platform
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

from settings import Setts

if platform.system() == "Windows":
    from uninstall import uninstall_win as uninstall_mod

class Connector(QObject):

    #
    #

    def __init__(self):
        QObject.__init__(self)
        self.setts = Setts()
        self.Uninst = uninstall_mod.Uninstaller(self.setts.parent_folder,
                                                self.setts.passcode,
                                                self.setts.server[1]['path'])


    update = pyqtSignal(int, arguments=['updater'])
    done = pyqtSignal(int, arguments=['doner'])

    def doner(self, lev):
        self.done.emit(lev)

    def updater(self, per):
        self.update.emit(per)

    @pyqtSlot()
    def start_server_uninstall(self):
        st_t = threading.Thread(target=self._start_uninstall)
        st_t.daemon = True
        st_t.start()

    def _start_uninstall(self):
        self.stop_server()
        self.updater(10)
        sleep(.3)
        self.del_files()
        sleep(.2)
        self.updater(30)
        sleep(.2)
        self.updater(50)
        sleep(.3)
        self.updater(70)
        sleep(3)
        self.updater(100)
        # check if all is well
        self.doner(7)

    def stop_server(self):
        stop_t = threading.Thread(target=self._stop_server)
        stop_t.daemon = True
        stop_t.start()

    def _stop_server(self):
        self.Uninst.stop_server()

    def del_files(self):
        del_t = threading.Thread(target=self._del_files)
        del_t.daemon = True
        del_t.start()

    def _del_files(self):
        self.Uninst.del_files()
